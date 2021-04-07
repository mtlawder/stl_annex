import pandas as pd
import sqlite3
from bokeh.plotting import figure, ColumnDataSource
from bokeh.embed import components
from bokeh.palettes import Category20
from bokeh.io import curdoc
from bokeh.transform import cumsum
from bokeh.models import HoverTool
import holoviews as hv
import panel as pn
from math import pi
hv.extension('bokeh')

def apply_style(plot, element):
    plot.state.toolbar_location = None
    plot.state.background_fill_alpha=0
    plot.state.border_fill_alpha = 0

def passsenger_flow_all(ap2,reg_main_select,advanced_select,carrier_select):
    conn=sqlite3.connect('passenger_flow.db')
    whereClause = f'begin="{ap2}"'
    whereClauseT100 = f'AIRPORT_PAIR="{ap2}"'
    print(advanced_select)
    valid_data=1
    if advanced_select=='true':
        print('c')
        if carrier_select!='ALL':
            whereClause+=f' AND carrier="{carrier_select}"'
            whereClauseT100+=f' AND CARRIER="{carrier_select}"'
    print('WHERE')
    print(whereClause)
    result=pd.read_sql(f'SELECT begin,sum(passengers_end) AS passengers_end,sum(passengers_continue) as passengers_continue, \
        sum(passengers_total) as passengers_total FROM route_flow_summary WHERE {whereClause} GROUP BY begin',conn)
    try:
        total_pass=result['passengers_total'][0]
    except:
        valid_data=0
        t100_data={"Year":'2019',"Passengers": '0', "Seats":'0', "Departures":'0',
        "Load Factor":'0%'}
        
        return '','','','','','','','0','0','0%',t100_data,valid_data
    route_pass_end=result['passengers_end'][0]
    emon=[(0,1,total_pass),(1,2,route_pass_end),(1,3,result['passengers_continue'][0])]
    elab=[ap2, "STL", "STL (final dest)", "Connecting via STL"]
    con_det=pd.read_sql(f'SELECT * FROM connecting_detail WHERE {whereClause}',conn)
    con_det=con_det[con_det['first_connect']==1]
    con_det=con_det.groupby(['begin','end']).agg({'passengers':sum})
    con_det=con_det.sort_values('passengers',ascending=False).reset_index()

    num_detail=12
    rest_cities=sum(con_det[num_detail:]['passengers'])
    for i in range(0,num_detail):
        emon+=[(3,4+i,con_det['passengers'][i])]
        elab+=[con_det['end'][i]]
    emon+=[(3,5+i,rest_cities)]
    elab+=['Other']

    nodes = hv.Dataset(enumerate(elab), 'index', 'label')
    value_dim = hv.Dimension('Passengers')

    h2=hv.Sankey((emon, nodes), ['From', 'To'], vdims=value_dim).options(
        label_index='label', label_position='left', width=700, height=600, edge_color_index='To',tools=['reset']
    )
    renderer = hv.renderer('bokeh')
    
    h2.opts(default_tools = ['hover'])
    h2a=h2.opts(plot=dict(hooks=[apply_style]))
    fp=pn.Row(h2a)
    doc = curdoc()
    script,div=components(fp.get_root(doc))
    table_data=con_det.to_json(orient='split')
    od_market_pass=pd.read_sql(f'SELECT PASSENGERS from od_market_totals WHERE ORIGIN="{ap2}"',conn)
    od_pass=od_market_pass['PASSENGERS'][0]
    t100_result=pd.read_sql(f'SELECT YEAR, sum(PASSENGERS) as "PASS",sum(SEATS) as "SEATS",sum(DEPARTURES_PERFORMED) as "DEPTS" \
        FROM route_detail WHERE {whereClauseT100} AND DIRECTION="ARRIVE" GROUP BY YEAR',conn)
    yr_range=pd.DataFrame([str(x) for x in range(2010,2020)],columns=['YEAR'])
    t100_result=yr_range.merge(t100_result,how='left',on='YEAR').fillna(0)
    t100_now=t100_result[t100_result['YEAR']=='2019'].reset_index()
    t100_data={"Year":t100_now['YEAR'][0],"Passengers": t100_now['PASS'][0], "Seats":t100_now['SEATS'][0], "Departures":t100_now['DEPTS'][0],
        "Load Factor":t100_now['PASS'][0]/t100_now['SEATS'][0]}
    # t100_data=t100_result.to_json(orient='split')

    p1 = figure(x_range=list(t100_result['YEAR'].astype(str)), plot_height=350,
        plot_width=600,title=f"Passenger Counts {ap2} to STL", toolbar_location=None, tools="")
    d_source=ColumnDataSource({'x':t100_result['YEAR'].astype(str),
                    'y':t100_result['PASS']/1000})
    p=p1.vbar(x='x', top='y', source=d_source, width=0.85,fill_alpha=0.8)
    p1.add_tools(HoverTool(tooltips=[("Year",'@x'),("Passengers", "@y{,0}k")],renderers=[p]))
    p1.xgrid.grid_line_color = None
    p1.y_range.start = 0
    p1.xaxis.major_label_orientation = 1.2
    p1.background_fill_alpha=0
    p1.border_fill_alpha = 0
    p1.yaxis.axis_label= "Thousands of Passengers"
    script_t100, div_t100 = components(p1)

    # reg_main_select='x'
    div_pie,script_pie=pie_carrier_plots(ap2,reg_main_select,advanced_select,carrier_select)

    return div,script,div_t100,script_t100,div_pie,script_pie,table_data,total_pass,od_pass,route_pass_end,t100_data,valid_data

def pie_carrier_plots(ap2,reg_main_select,advanced_select,carrier_select):
    conn_pie=sqlite3.connect('passenger_flow.db')
    whereClause = f'begin="{ap2}"'
    whereClauseT100 = f'AIRPORT_PAIR="{ap2}"'
    
    if advanced_select:
        if carrier_select!='ALL':
            whereClause+=f' AND carrier="{carrier_select}"'
            whereClauseT100+=f' AND CARRIER="{carrier_select}"'
    if reg_main_select=='regional':
        pie_result=pd.read_sql(f'SELECT CARRIER,PASSENGERS FROM route_detail WHERE AIRPORT_PAIR="{ap2}" AND \
            YEAR="2019" AND DIRECTION="ARRIVE" AND PASSENGERS>0',conn_pie)
    else:
        pie_result=pd.read_sql(f'SELECT TICKET_CARRIER AS CARRIER,SUM(PASSENGERS_ADJ) AS PASSENGERS FROM route_detail_mainline_adj WHERE AIRPORT_PAIR="{ap2}" AND \
            YEAR="2019" AND DIRECTION="ARRIVE" AND PASSENGERS>0 GROUP BY TICKET_CARRIER',conn_pie)
        # pie_result['CARRIER']=pie_result['TICKET_CARRIER']
        # pie_result['PASSENGERS']=pie_result['PASSENGERS_ADJ']
    pie_result['angle']=pie_result['PASSENGERS']/pie_result['PASSENGERS'].sum()*2*pi
    pie_result['percent']=pie_result['PASSENGERS']/pie_result['PASSENGERS'].sum()
    pie_result['color']='red'
    for i in range(0,len(pie_result)):
        pie_result['color'][i]=Category20[10][i%10]

    plot=figure(title='Carriers 2019',x_range=(0,3.3),y_range=(0.5,1.5),width=300,height=250,tools='')
    plot.outline_line_color = None
    legend=plot.wedge(x=2,y=1,radius=1.2,start_angle=cumsum('angle', include_zero=True),\
        end_angle=cumsum('angle'),fill_color='color',line_color='white',source=pie_result,legend_field='CARRIER')
    plot.add_tools(HoverTool(tooltips=[("Airline","@CARRIER"),("Passengers", "@PASSENGERS{0,f}"),
                                    ("Pass %","@percent{%f}")],renderers=[legend]))
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = None
    plot.legend.location='top_left'
    plot.toolbar_location=None
    plot.axis.visible = False
    plot.title.align='center'
    plot.background_fill_alpha=0
    plot.border_fill_alpha = 0
    script_pie, div_pie = components(plot)

    return div_pie,script_pie