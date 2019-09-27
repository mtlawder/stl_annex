import pandas as pd
import numpy as np
from bokeh.plotting import show, figure, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category20

airport='STL'
airline='F9'

def year_over_year_chart(summary_df,dest_col,airport,airline):
    passengers=table_out.pivot(index='DESTINATION',columns='YEAR',values='PASSENGERS')
    departures=table_out.pivot(index='DESTINATION',columns='YEAR',values='DEPARTURES')
    load_factor=table_out.pivot(index='DESTINATION',columns='YEAR',values='LOAD FACTOR')
    airports=list(set(summary_df[dest_col]))
    pass_source=ColumnDataSource(passengers.transpose())
    dept_source=ColumnDataSource(departures.transpose())
    lf_source=ColumnDataSource(load_factor.transpose())
    y_max_p,y_max_d=0,0
    for year in range(2014,2019):
        local_max=max(passengers.fillna(0)[year])
        if local_max>y_max_p:
            y_max_p=local_max
    for year in range(2014,2019):
        local_max=max(departures.fillna(0)[year])
        if local_max>y_max_d:
            y_max_d=local_max
    pass_fig=figure(x_range=(2014,2019.1),y_range=(0,y_max_p+5000),width=425,height=400,\
                    title="Passengers flying out of "+airport+" on "+airline)
    pass_fig.left[0].formatter.use_scientific =False
    pass_fig.toolbar_location = None
    pass_fig.xaxis.axis_label = 'YEAR'
    pass_fig.yaxis.axis_label = 'Passengers'
    dept_fig=figure(x_range=(2014,2018.1),y_range=(0,y_max_d+100),width=370,height=400,\
                     title=airline+" Departures flying out of "+airport)
    dept_fig.left[0].formatter.use_scientific =False
    dept_fig.toolbar_location = None
    dept_fig.xaxis.axis_label = 'YEAR'
    dept_fig.yaxis.axis_label = 'Departures'
    lf_fig=figure(x_range=(2014,2018.1),y_range=(50,100),width=370,height=400,\
                    title="Load Factor for "+airline+" routes from "+airport)
    lf_fig.left[0].formatter.use_scientific =False
    lf_fig.toolbar_location = None
    lf_fig.xaxis.axis_label = 'YEAR'
    lf_fig.yaxis.axis_label = 'Load Factor'
    color_cnt=0


    for dest in airports:
        p=pass_fig.line(x='YEAR',y=dest,source=pass_source,color=Category20[15][color_cnt%15],line_width=3,legend=dict(value=dest))
        pass_fig.add_tools(HoverTool(tooltips=[('Dest',dest),('Passengers','@'+dest)],renderers=[p]))
        p=dept_fig.line(x='YEAR',y=dest,source=dept_source,color=Category20[15][color_cnt%15],line_width=3)
        dept_fig.add_tools(HoverTool(tooltips=[('Dest',dest),('Passengers','@'+dest)],renderers=[p]))
        p=lf_fig.line(x='YEAR',y=dest,source=lf_source,color=Category20[15][color_cnt%15],line_width=3)
        lf_fig.add_tools(HoverTool(tooltips=[('Dest',dest),('Passengers','@'+dest)],renderers=[p]))
        color_cnt+=1
    pass_fig.legend.label_text_font_size = '9pt'
    pass_fig.legend.glyph_width=6
    output_file('By the Numbers Blogs/'+airport+'_'+airline+'_pass.html')
    show(pass_fig)
    output_file('By the Numbers Blogs/'+airport+'_'+airline+'_dept.html')
    show(dept_fig)
    output_file('By the Numbers Blogs/'+airport+'_'+airline+'_lf.html')
    show(lf_fig)
    return passengers,departures,load_factor

def totaling_flights_by_year(df):
    yearly_totals=df.groupby(['DESTINATION','YEAR']).agg({'DEPARTURES_PERFORMED':np.sum,'PASSENGERS':np.sum\
                    ,'SEATS':np.sum,'RAMP_TO_RAMP':np.sum,'AIR_TIME':np.sum,'CITY':'first'})
#     yearly_totals.columns=yearly_totals.columns.droplevel(1)
    yearly_totals=yearly_totals.reset_index()
    yearly_totals['LOAD FACTOR']=(yearly_totals['PASSENGERS']/yearly_totals['SEATS'])*100
    yearly_totals['DEPARTURES']=yearly_totals['DEPARTURES_PERFORMED'].astype(int)
    yearly_totals['PASSENGERS']=yearly_totals['PASSENGERS'].astype(int)
    yearly_totals['AVG TRIP TIME']=yearly_totals['RAMP_TO_RAMP']/yearly_totals['DEPARTURES_PERFORMED']
    yearly_totals['AVG TAXI TIME']=(yearly_totals['RAMP_TO_RAMP']-yearly_totals['AIR_TIME'])/yearly_totals['DEPARTURES_PERFORMED']
    table_out=yearly_totals.loc[yearly_totals['DEPARTURES']>10]
    return table_out

def aircraft_type(origin_df,dest_df):
    aircraft_lookup=pd.read_csv('AIRCRAFT LOOKUP csv')
    aircraft_origin=origin_df.groupby(['AIRCRAFT_TYPE','YEAR']).agg({'PASSENGERS':np.sum,'SEATS':np.sum\
                    ,'DEPARTURES_PERFORMED':np.sum}).reset_index()
    aircraft_origin=aircraft_origin.merge(aircraft_lookup,left_on="AIRCRAFT_TYPE",right_on="Code")
    aco=aircraft_origin.loc[aircraft_origin['YEAR']==2018]
    aircraft_dest=dest_df.groupby(['AIRCRAFT_TYPE','YEAR']).agg({'PASSENGERS':np.sum,'SEATS':np.sum\
                    ,'DEPARTURES_PERFORMED':np.sum}).reset_index()
    aircraft_dest=aircraft_dest.merge(aircraft_lookup,left_on="AIRCRAFT_TYPE",right_on="Code")
    acd=aircraft_dest.loc[aircraft_dest['YEAR']==2018]
    aircraft_combined=aco.merge(acd,on="Code",suffixes=('_o','_d'))
    aircraft_combined['Airplane']=aircraft_combined['Description_o']
    aircraft_combined['Departures']=(aircraft_combined['DEPARTURES_PERFORMED_o']+aircraft_combined['DEPARTURES_PERFORMED_d']).astype(int)
    aircraft_combined['Passengers']=(aircraft_combined['PASSENGERS_o']+aircraft_combined['PASSENGERS_d']).astype(int)
    aircraft_combined['Load Factor']=(aircraft_combined['Passengers']/(aircraft_combined['SEATS_o']+aircraft_combined['SEATS_d']))*100
    aircraft_combined['% Passengers']=(aircraft_combined['Passengers']/aircraft_combined['Passengers'].sum())*100
    aircraft_combined['% Departures']=(aircraft_combined['Departures']/aircraft_combined['Departures'].sum())*100
    return aircraft_combined[['Airplane','Departures','% Departures','Passengers','% Passengers','Load Factor']]

print('Loading full db')
df = pd.read_csv('T-100 Segments file')
print('db loaded')

stl_origin_df=df.loc[df['ORIGIN']==airport]
stl_dest_df=df.loc[df['DEST']==airport]
stl_origin_car_df=stl_origin_df.loc[stl_origin_df['UNIQUE_CARRIER']==airline]
origin_by_year_df=stl_origin_car_df.groupby(['DEST','YEAR']).agg({'PASSENGERS':np.sum,'SEATS':np.sum\
                ,'DEPARTURES_PERFORMED':np.sum,'RAMP_TO_RAMP':np.sum,'AIR_TIME':np.sum,'DEST_CITY_NAME':'first'}).reset_index()
stl_dest_car_df=stl_dest_df.loc[stl_dest_df['UNIQUE_CARRIER']==airline]
dest_by_year_df=stl_dest_car_df.groupby(['ORIGIN','YEAR']).agg({'PASSENGERS':np.sum,'SEATS':np.sum\
                ,'DEPARTURES_PERFORMED':np.sum,'RAMP_TO_RAMP':np.sum,'AIR_TIME':np.sum,'ORIGIN_CITY_NAME':'first'}).reset_index()
origin_by_year_df['DESTINATION']=origin_by_year_df['DEST']
origin_by_year_df['CITY']=origin_by_year_df['DEST_CITY_NAME']
origin_by_year_df['DIRECTION']=['DEPART']*len(origin_by_year_df['DEST'])
dest_by_year_df['DESTINATION']=dest_by_year_df['ORIGIN']
dest_by_year_df['CITY']=dest_by_year_df['ORIGIN_CITY_NAME']
dest_by_year_df['DIRECTION']=['ARRIVE']*len(dest_by_year_df['ORIGIN'])
combined_by_year_df=origin_by_year_df.append(dest_by_year_df).drop(['DEST','ORIGIN'], axis=1)
#Arriving flights only
table_out_arrive=totaling_flights_by_year(combined_by_year_df.loc[combined_by_year_df['DIRECTION']=='ARRIVE'])
#Departing Flights only
table_out_depart=totaling_flights_by_year(combined_by_year_df.loc[combined_by_year_df['DIRECTION']=='DEPART'])
#COMBINED
table_out=totaling_flights_by_year(combined_by_year_df)
print('yoy tables built')

formatters={'PASSENGERS':lambda x: '{:,}'.format(x),'LOAD FACTOR':lambda x: '{:,.1f}'.format(x)\
           ,'AVG TRIP TIME':lambda x: '{:,.1f}'.format(x), 'AVG TAXI TIME':lambda x: '{:,.1f}'.format(x)}
table_out.loc[table_out['YEAR']==2018][['DESTINATION','CITY','PASSENGERS','LOAD FACTOR','DEPARTURES','AVG TRIP TIME'\
    ,'AVG TAXI TIME']].to_html('By the Numbers Blogs/'+airport+'_'+airline+'_2018_combined_stats.html', index=False\
    ,formatters=formatters)
table_out_arrive.loc[table_out_arrive['YEAR']==2018][['DESTINATION','CITY','PASSENGERS','LOAD FACTOR','DEPARTURES','AVG TRIP TIME'\
    ,'AVG TAXI TIME']].to_html('By the Numbers Blogs/'+airport+'_'+airline+'_2018_combined_stats_arrivals.html', index=False\
    ,formatters=formatters)
table_out_depart.loc[table_out_depart['YEAR']==2018][['DESTINATION','CITY','PASSENGERS','LOAD FACTOR','DEPARTURES','AVG TRIP TIME'\
    ,'AVG TAXI TIME']].to_html('By the Numbers Blogs/'+airport+'_'+airline+'_2018_combined_stats_departures.html', index=False\
    ,formatters=formatters)

aircraft_df=aircraft_type(stl_origin_car_df,stl_dest_car_df)
print('aircraft type table built')
formatters={'Passengers':lambda x: '{:,}'.format(x),'Load Factor':lambda x: '{:,.1f}'.format(x)\
           ,'Departures':lambda x: '{:,}'.format(x), '% Passengers':lambda x: '{:,.1f}'.format(x)\
           ,'% Departures':lambda x: '{:,.1f}'.format(x)}
aircraft_df.to_html('By the Numbers Blogs/'+airport+'_'+airline+'_2018_aircraft_type.html', index=False\
    ,formatters=formatters)

p,d,lf=year_over_year_chart(table_out,'DESTINATION',airport,airline)
print('PAX')
print(p)
print('DEPTS')
print(d)
print('LOAD FACTOR')
print(lf)