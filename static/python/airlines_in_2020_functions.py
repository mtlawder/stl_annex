from bokeh.plotting import figure, ColumnDataSource
from bokeh.embed import components
from bokeh.models import HoverTool, NumeralTickFormatter
from bokeh.palettes import Category10
from bokeh.transform import dodge
import pandas as pd
import sqlite3

def airline_chart(df19,df20,col_type,hover,label,t_form,airport):
    month_labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    source=ColumnDataSource({'month_19':list(zip(df19['MONTH_labels'],[-0.2]*12)),
                'pass_19':df19[col_type],'pass_20':df20[col_type],
                'month_20':list(zip(df20['MONTH_labels'],[0.2]*12)),'month':month_labels})
    f_pass=figure(title=airport+' '+label,x_range=df19['MONTH_labels'],tools='reset',height=330,width=470)
    p=f_pass.vbar(x='month_19',top='pass_19',source=source, width=0.4,color="#0087c4",line_width=1,
                  line_color="#004d70",alpha=0.8,legend_label='2019')
    p2=f_pass.vbar(x='month_20',top='pass_20',source=source, width=0.4,color='#ce5555',line_width=1,
                  line_color="#6d2d2d",alpha=0.8,legend_label='2020')
    f_pass.add_tools(HoverTool(tooltips=[("Month", "@month"),(hover+" '19", "@pass_19{,f}"),(hover+" '20", "@pass_20{,f}"),
                                     ],renderers=[p,p2]))
    f_pass.xgrid.grid_line_color = None
    f_pass.legend.location='bottom_left'
    f_pass.toolbar_location=None
    f_pass.y_range.start=0
    f_pass.border_fill_alpha = 0
    f_pass.background_fill_color ='#f7f7f7'
    f_pass.yaxis.axis_label="Total "+label
    f_pass.yaxis.formatter=NumeralTickFormatter(format=t_form)
    return components(f_pass)

def airline_2020_comp_chart(airports):
    airports=[x for x in airports if x!='']
    airports_join="','".join(airports)
    conn=sqlite3.connect('airport_comp_2020.db')
    airport_table=pd.read_sql(f"SELECT * FROM monthly_2020_2019_airport_comp WHERE AIRPORT IN ('{airports_join}')",conn)
    latest_year=max(airport_table['YEAR'])
    latest_month=max(airport_table.loc[airport_table['YEAR']==latest_year]['MONTH'])
    month_labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    a_2020=airport_table.loc[airport_table['YEAR']==max(airport_table['YEAR'])].copy()
    send_df=a_2020.groupby(['AIRPORT','MONTH']).agg({'PASSENGERS':sum,'SEATS':sum,'DEPARTURES_PERFORMED':sum}).reset_index()
    f_pass=figure(title='2020 Monthly Passenger Totals',tools='reset',height=425,x_range=month_labels)
    move=-0.8
    colors=Category10[4]
    tal=0
    for airp in airports:
        temp_df=send_df.loc[send_df['AIRPORT']==airp].copy()
        source=ColumnDataSource({airp:temp_df['PASSENGERS'],'Month':temp_df['MONTH'],"Month_l":month_labels[:latest_month]})
        p=f_pass.vbar(x=dodge('Month', move, range=f_pass.x_range),top=airp,source=source,width=0.18,
                      color=colors[tal],legend_label=airp,alpha=0.8)
        f_pass.add_tools(HoverTool(tooltips=[("Year","2020"),("Month", "@Month_l"),(airp, "@"+airp+"{,f}")],renderers=[p]))
        move+=0.22
        tal+=1    
    f_pass.xgrid.grid_line_color = None
    f_pass.legend.location='top_right'
    f_pass.toolbar_location=None
    f_pass.y_range.start=0
    f_pass.yaxis.axis_label="Monthly Passengers"
    f_pass.yaxis.formatter=NumeralTickFormatter(format='0.0a')
    f_pass.border_fill_alpha = 0
    f_pass.background_fill_color ='#f7f7f7'
    airport_comp_script,airport_comp_div=components(f_pass)
    return airport_comp_script,airport_comp_div

def airline_2020_comp(airport):
    conn=sqlite3.connect('airport_comp_2020.db')
    airport_table=pd.read_sql(f"SELECT * FROM monthly_2020_2019_airport_comp WHERE AIRPORT='{airport}'",conn)
    latest_year=max(airport_table['YEAR'])
    latest_month=max(airport_table.loc[airport_table['YEAR']==latest_year]['MONTH'])
    a_2020=airport_table.loc[airport_table['YEAR']==max(airport_table['YEAR'])].copy()
    a_2019=airport_table.loc[airport_table['YEAR']==max(airport_table['YEAR']-1)].copy()
    a_2019=a_2019.loc[a_2019['MONTH']<=latest_month].copy()
    send_df=a_2020.groupby('AIRPORT').agg({'PASSENGERS':sum,'SEATS':sum,'DEPARTURES_PERFORMED':sum}).reset_index()
    send_df2=a_2019.groupby('AIRPORT').agg({'PASSENGERS':sum,'SEATS':sum,'DEPARTURES_PERFORMED':sum}).reset_index()
    send_df=send_df.merge(send_df2,on='AIRPORT',suffixes=('_20','_19'))
    send_df=send_df.set_index('AIRPORT')
    send_df['Pct Chg YTD Pass']=(send_df['PASSENGERS_20']-send_df['PASSENGERS_19'])/send_df['PASSENGERS_19']
    send_df['Pct Chg YTD Seats']=(send_df['SEATS_20']-send_df['SEATS_19'])/send_df['SEATS_19']
    send_df['Pct Chg YTD Flights']=(send_df['DEPARTURES_PERFORMED_20']-send_df['DEPARTURES_PERFORMED_19'
                                    ])/send_df['DEPARTURES_PERFORMED_19']
    send_df.columns=['2020 Passengers', '2020 Seat Capacity', '2020 Flights', '2019 Passengers',
           '2019 Seat Capacity', '2019 Flights', 'Pct Chg YTD Pass',
           'Pct Chg YTD Seats', 'Pct Chg YTD Flights']
    return send_df

def airlines_in_2020_content(air_sel):
    conn=sqlite3.connect('airport_comp_2020.db')
    airports=pd.read_sql("SELECT DISTINCT(A.AIRPORT),B.DISPLAY_AIRPORT_NAME FROM monthly_2020_2019_airport_comp as A "+
                 "LEFT JOIN airport_names as B ON A.AIRPORT=B.AIRPORT ORDER BY A.AIRPORT",conn)
    airport_list=airports.to_json(orient='split')
    airport_table=pd.read_sql(f"SELECT * FROM monthly_2020_2019_airport_comp WHERE AIRPORT='{air_sel}'",conn)
    latest_year=max(airport_table['YEAR'])
    latest_month=max(airport_table.loc[airport_table['YEAR']==latest_year]['MONTH'])
    months_full=['January','February','March','April','May','June','July','August','September','October','November','December']
    latest_month_label=months_full[latest_month-1]
    m_totals=airport_table.loc[airport_table['MONTH']==latest_month].copy()
    a_totals=m_totals.groupby(['YEAR','AIRPORT']).agg({'PASSENGERS':sum,'SEATS':sum,'DEPARTURES_PERFORMED':sum,
                                         'DEPARTURES_SCHEDULED':sum}).reset_index()
    acols=['Year','AIRPORT','Passengers','Seat Capacity','Flights Completed','Sch Flights']
    a_totals.columns=acols
    a_totals['Cancelled Flights']=a_totals['Sch Flights']-a_totals['Flights Completed']
    pcts=pd.DataFrame({'Passengers':[a_totals['Passengers'].pct_change()[1]],
                  'Seat Capacity':[a_totals['Seat Capacity'].pct_change()[1]],
                  'Flights Completed':[a_totals['Flights Completed'].pct_change()[1]],
                  'Cancelled Flights':[a_totals['Cancelled Flights'].pct_change()[1]],
                      'Year':['Pct Change']})
    a_totals['Year']=a_totals["Year"].astype('str')
    # a_totals=a_totals.append(pcts)[['Year','Flights Completed','Cancelled Flights','Seat Capacity','Passengers']]
    a_totals=a_totals.append(pcts)[['Year','Passengers','Seat Capacity','Flights Completed']]
    totals_display=a_totals.to_json(orient='split')

    plot_totals=airport_table.groupby(['YEAR','MONTH']).agg({'PASSENGERS':sum,'SEATS':sum,'DEPARTURES_PERFORMED':sum,
                                     'DEPARTURES_SCHEDULED':sum}).reset_index()
    plot_totals['Cancelled Flights']=plot_totals['DEPARTURES_SCHEDULED']-plot_totals['DEPARTURES_PERFORMED']
    month_labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    plot_totals['MONTH_labels']=plot_totals['MONTH'].apply(lambda x: month_labels[(x-1)%12])
    plot_totals_19=plot_totals.loc[plot_totals['YEAR']==2019].copy()
    plot_totals_20=plot_totals.loc[plot_totals['YEAR']==2020].copy()
    plot_totals_20=plot_totals_19[['MONTH_labels']].merge(plot_totals_20,how='left',on='MONTH_labels').fillna(0)

    pass_script,pass_div=airline_chart(plot_totals_19,plot_totals_20,'PASSENGERS','Pass','Passengers','0.0a',air_sel) 
    dept_script,dept_div=airline_chart(plot_totals_19,plot_totals_20,'DEPARTURES_PERFORMED','Dept','Departures','0a',air_sel)
    seats_script,seats_div=airline_chart(plot_totals_19,plot_totals_20,'SEATS','Seats','Seat Capacity','0.0a',air_sel)
    # canc_script,canc_div=airline_chart(plot_totals_19,plot_totals_20,'Cancelled Flights','X Flights','Cancelled Flights','0')


    airports2=pd.read_sql("SELECT DISTINCT(A.AIRPORT2),B.DISPLAY_AIRPORT_NAME FROM monthly_2020_2019_airport_comp as A "+
                    f"LEFT JOIN airport_names as B ON A.AIRPORT2=B.AIRPORT WHERE A.AIRPORT='{air_sel}'",conn)
    ytd=airport_table.loc[airport_table['MONTH']<=latest_month]
    lm=airport_table.loc[airport_table['MONTH']==latest_month]
    ytd
    ytd=ytd.groupby(['YEAR','AIRPORT2']).agg({'PASSENGERS':sum,'SEATS':sum,'DEPARTURES_PERFORMED':sum,
                                         'DEPARTURES_SCHEDULED':sum}).reset_index()
    ytd_pivot=ytd.pivot(index='AIRPORT2',columns='YEAR',values='PASSENGERS').reset_index().rename(columns={2019:
        'Pass_19',2020:'Pass_20'}).merge(ytd.pivot(index='AIRPORT2',columns='YEAR',values='SEATS').reset_index().rename(
        columns={2019:'Seats_19',2020:'Seats_20'}),on='AIRPORT2').merge(ytd.pivot(index='AIRPORT2',columns='YEAR',values=
        'DEPARTURES_PERFORMED').reset_index().rename(columns={2019:'Dept_19',2020:'Dept_20'}),on='AIRPORT2')
    lm_pivot=lm.pivot(index='AIRPORT2',columns='YEAR',values='PASSENGERS').reset_index().rename(columns={2019:
        'Pass_19',2020:'Pass_20'}).merge(lm.pivot(index='AIRPORT2',columns='YEAR',values='SEATS').reset_index().rename(
        columns={2019:'Seats_19',2020:'Seats_20'}),on='AIRPORT2').merge(lm.pivot(index='AIRPORT2',columns='YEAR',values=
        'DEPARTURES_PERFORMED').reset_index().rename(columns={2019:'Dept_19',2020:'Dept_20'}),on='AIRPORT2')
    routes_df=ytd_pivot.merge(lm_pivot,how='left',on='AIRPORT2',suffixes=('_ytd','_m')).fillna(0).sort_values(
        'Pass_20_ytd',ascending=False)
    routes_df=routes_df.merge(airports2,how='left',on='AIRPORT2')
    routes_display=routes_df.to_json(orient='split')
    return totals_display,pass_script,pass_div,dept_script,dept_div,seats_script,seats_div,airport_list,routes_display, latest_month_label