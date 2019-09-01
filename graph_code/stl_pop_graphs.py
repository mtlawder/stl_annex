################################
# GRAPHS FOR STL_POP PAGE
# MATT LAWDER 8-19-2019
################################

from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot
from bokeh.embed import components
from bokeh.models import Range1d
from bokeh.document import Document
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool, FixedTicker
from bokeh.palettes import Category10, Category20
from bokeh.transform import cumsum
from math import pi
import collections
import pandas as pd
import numpy as np
import sqlite3


nbhood="Midtown"
conn=sqlite3.connect('stl_census.db')
dd=pd.read_sql('SELECT * FROM neighborhood_pop',conn)
nb=dd.loc[dd['Neighborhood']==nbhood]

#Line Chart of Pop changes
p2=figure(title="Population of "+nbhood, width=400, height=350)
nb['Total_Population']=nb['Total Population'].apply(lambda s: int(s.replace(',','')))
nb['Black_Total']=nb['Black Total'].apply(lambda s: int(s.replace(',','')))
nb['White_Total']=nb['White Total'].apply(lambda s: int(s.replace(',','')))
nb['Other_Total']=nb['Other Total']
source=ColumnDataSource(nb)
color_cnt=0
for pop in ['Total_Population','Black_Total','White_Total','Other_Total']:
    p=p2.line(x='Year',y=pop,source=source,color=Category10[5][color_cnt%5],line_wdth="3",legend={'value':pop})
    hover='@'+pop
    p2.add_tools(HoverTool(tooltips=[(str(pop),hover)],renderers=[p]))
    color_cnt+=1
show(p2)

#Pie Charts
plots={}
legend={}
for yr in [1990,2000,2010]:
    x=collections.OrderedDict()
    if yr == 1990:
        vals=['Black Total','White Total','Other']
        nb['Other']=nb['Other Total']
        single=nb.loc[nb['Year']==str(yr)]
        single=single.reset_index()
# required for Order Dict
        for xp in vals:
            x[xp]=int(single[xp][0])
#         x={x:int(single[x][0]) for x in vals}
        data=pd.Series(x).reset_index(name='value').rename(columns={'index':'people'})
    else:
        vals=['Black Total','White Total','Other','Asian','Native American','Pacific Islander','Two or more']
        nb['Other']=nb['A Other']
        single=nb.loc[nb['Year']==str(yr)]
        single=single.reset_index()
        for xp in vals:
            x[xp]=int(single[xp][0].replace(',',''))
#         x={x:int(single[x][0].replace(',','')) for x in vals}
        data=pd.Series(x).reset_index(name='value').rename(columns={'index':'people'})
    data['angle']=data['value']/data['value'].sum()*2*pi
    data['color']=Category20[len(x)]
    start_angle=[data['angle'][:x].sum() for x in range(0,len(data['angle']))]
    end_angle=[data['angle'][:x+1].sum() for x in range(0,len(data['angle']))]
    
    if yr==2010:
        plots[yr]=figure(title="Pop "+str(yr),x_range=(-1,3),y_range=(0.2,1.8),width=210,height=150)
        legend[yr]=plots[yr].wedge(x=0.2,y=1,radius=1,start_angle=cumsum('angle', include_zero=True),\
            end_angle=cumsum('angle'),fill_color='color',line_color='white',legend='people',source=data)
    else:
        plots[yr]=figure(title="Pop "+str(yr),width=160,height=150)
        legend[yr]=plots[yr].wedge(x=0,y=1,radius=0.7,start_angle=cumsum('angle', include_zero=True),\
            end_angle=cumsum('angle'),fill_color='color',line_color='white',source=data)
    plots[yr].axis.axis_label=None
    plots[yr].axis.visible=False
    plots[yr].grid.grid_line_color = None
    plots[yr].legend.location= 'center_right'
show(gridplot([[plots[1990],plots[2000],plots[2010]]]))
