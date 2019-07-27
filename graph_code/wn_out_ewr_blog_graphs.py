######################################
# Plots for Southwest Leaving Newark
# Matt Lawder
######################################

import pandas as pd
import numpy as np
from bokeh.plotting import show, figure, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import gridplot
from bokeh.palettes import Category20

##ACCESS to full T100 Domestic data required, not accessible currently (7/26/2019) via db
df = pd.read_csv('T-100 data\Combined T100D-Segements.csv')

sw_df=df.loc[df['UNIQUE_CARRIER']=='WN']
city_df=sw_df.loc[sw_df['ORIGIN']=='EWR']
summary_df=city_df.groupby(['DEST','YEAR'])['SEATS','PASSENGERS','DEPARTURES_PERFORMED'].agg({'total':np.sum})
summary_df.columns=summary_df.columns.droplevel(0)
summary_df=summary_df.reset_index()
summary_df=summary_df.loc[summary_df['DEPARTURES_PERFORMED']>40]
summary_df['LOAD_FACTOR']=summary_df['PASSENGERS']/summary_df['SEATS']

# Create individual df's plot use in ColumnDataSource
passengers=summary_df.pivot(index='DEST',columns='YEAR',values='PASSENGERS')
departures=summary_df.pivot(index='DEST',columns='YEAR',values='DEPARTURES_PERFORMED')
load_factor=summary_df.pivot(index='DEST',columns='YEAR',values='LOAD_FACTOR')

airports=list(set(summary_df['DEST']))
pass_source=ColumnDataSource(passengers.transpose())
dept_source=ColumnDataSource(departures.transpose())
lf_source=ColumnDataSource(load_factor.transpose())
pass_fig=figure(x_range=(2014,2018.9),y_range=(0,236000),title="Passengers flying out of EWR on Southwest")
pass_fig.left[0].formatter.use_scientific =False
pass_fig.toolbar_location = None
pass_fig.xaxis.axis_label = 'YEAR'
pass_fig.yaxis.axis_label = 'Passengers'
dept_fig=figure(x_range=(2014,2018.9),y_range=(0,2400), title="Southwest Departures flying out of EWR")
dept_fig.left[0].formatter.use_scientific =False
dept_fig.toolbar_location = None
dept_fig.xaxis.axis_label = 'YEAR'
dept_fig.yaxis.axis_label = 'Departures'
lf_fig=figure(x_range=(2014,2018.9),y_range=(0.5,1),title="Load Factor for Southwest routes from EWR")
lf_fig.left[0].formatter.use_scientific =False
lf_fig.toolbar_location = None
lf_fig.xaxis.axis_label = 'YEAR'
lf_fig.yaxis.axis_label = 'Load Factor'
color_cnt=0


for dest in airports:
    p=pass_fig.line(x='YEAR',y=dest,source=pass_source,color=Category20[15][color_cnt],line_width=3,legend=dict(value=dest))
    pass_fig.add_tools(HoverTool(tooltips=[('Dest',dest),('Passengers','@'+dest)],renderers=[p]))
    p=dept_fig.line(x='YEAR',y=dest,source=dept_source,color=Category20[15][color_cnt],line_width=3,legend=dict(value=dest))
    dept_fig.add_tools(HoverTool(tooltips=[('Dest',dest),('Passengers','@'+dest)],renderers=[p]))
    p=lf_fig.line(x='YEAR',y=dest,source=lf_source,color=Category20[15][color_cnt],line_width=3,legend=dict(value=dest))
    lf_fig.add_tools(HoverTool(tooltips=[('Dest',dest),('Passengers','@'+dest)],renderers=[p]))
    color_cnt+=1
output_file('ewr_southwest_pass.html')
show(pass_fig)
output_file('ewr_southwest_dept.html')
show(dept_fig)
output_file('ewr_southwest_lf.html')
show(lf_fig)