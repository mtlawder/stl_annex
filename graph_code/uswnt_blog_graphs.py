######################################
# Plots for the USWNT Blog Post
# Matt Lawder
######################################

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource, Range1d, LinearAxis, Span
from bokeh.palettes import Category20

url="https://www.fifa.com/fifa-world-ranking/ranking-table/women/"
main_rep=requests.get(url=url)
main_soup=bs(main_rep.text,'html.parser')
date_tags=main_soup.find_all('li', {'class':'fi-ranking-schedule__nav__item'})
dates_url=[x.attrs['data-value'] for x in date_tags]
index=[]
country=[]
points=[]
prev_points=[]
change=[]
association=[]
date=[]
date_x=[]
combined_df=pd.DataFrame({'index':index,'country':country,'points':points,'prev_points':prev_points,\
              'change':change,'association':association,'date':date,'date_x':date_x})
for date_url in dates_url:
#     time.sleep(0.5)
    url="https://www.fifa.com/fifa-world-ranking/ranking-table/women/rank/"+date_url
    rank_rep=requests.get(url=url)
    rank_soup=bs(rank_rep.text,'html.parser')
    table=rank_soup.find('tbody').find_all('span',{'class':'text'})
    index=[]
    country=[]
    points=[]
    prev_points=[]
    change=[]
    association=[]
    date=[]
    date_x=[]
    for x in range(0,int(len(table)/7)):
        index+=[int(table[x*7].text)]
        country+=[table[x*7+1].find('span').text]
        points+=[int(table[x*7+2].text)]
        prev_points+=[int(table[x*7+3].text)]
        change+=[int(table[x*7+4].text)]
        association+=[table[x*7+6].text]
        date+=[date_url.split('_')[1]]
    new_frame=pd.DataFrame({'index':index,'country':country,'points':points,'prev_points':prev_points,\
                  'change':change,'association':association,'date':date})
    new_frame['date_x']=[x[:4]+'-'+x[4:6]+'-'+x[6:] for x in new_frame['date']]
    combined_df=combined_df.append(new_frame) 
    print(date_url)

# combined_df.to_csv('csv_file_path',encoding ='utf-8')
# combined_df=pd.read_csv('csv_file_path', encoding = "utf-8",dtype={'date':'object

date_set=list(set(combined_df['date']))
cset=combined_df.loc[combined_df['date']=='20190329']
country_set=list(set(cset.loc[cset['index']<41]['country']))
subset_dfs={}
for country in country_set:
    subset_dfs[country]=combined_df.loc[combined_df['country']==country]
plot_df=subset_dfs['USA'][['date_x']]
point_df=subset_dfs['USA'][['date_x']]
temp_df = []
temp_df2= []
for x in subset_dfs.keys():
    temp_df=subset_dfs[x]
    temp_df2=subset_dfs[x][:]
    temp_df[x]=subset_dfs[x]['index']
    temp_df2[x]=subset_dfs[x]['points']
    plot_df=pd.merge(plot_df,temp_df[['date_x',x]],on='date_x',how='outer')
    point_df=pd.merge(point_df,temp_df2[['date_x',x]],on='date_x',how='outer')
plot_df['date_x']=np.array(plot_df['date_x'],dtype=np.datetime64)
point_df['non_usa_max']=point_df.loc[:, point_df.columns != 'USA'].max(axis=1)
point_df['diff']=point_df['USA']-point_df['non_usa_max']
point_df['date_x']=np.array(point_df['date_x'],dtype=np.datetime64)


p1 = figure(x_axis_type="datetime", title="World Ranking", y_range=(0,20.5))
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Rank'
p2 = figure(x_axis_type="datetime", title="World Ranking Points", y_range=(1950,2280))
p2.grid.grid_line_alpha=0.3
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Points'
plot_xs=[]
plot_ys=[]
plot_cols=[]
plot_colors=[]
pdf=plot_df.to_dict(orient='list')
color_cnt=0
for x in subset_dfs:
    plot_xs+=[pdf['date_x']]
    plot_ys+=[pdf[x]]
    plot_cols+=[x]
    plot_colors+=[Category20[20][color_cnt%20]]
    color_cnt+=1
current_rank = [x[0] for x in plot_ys]
plot_dict={'x':plot_xs,'y':plot_ys,'cols':plot_cols,'colors':plot_colors,'curr':current_rank}
source=ColumnDataSource(data=plot_dict)

p1.multi_line('x','y',source=source,color='colors',line_width=2)
TOOL=[('Country','@cols'),('Current Rank','@curr')]

p1.add_tools(HoverTool(tooltips=TOOL,show_arrow=True,anchor='center'))
plot_xs2=[point_df.to_dict(orient='list')['date_x']]*3
plot_ys2=[point_df['USA'],point_df['diff']]
plot_cols2=['USA points','margin']
plot_colors2=['red','blue']
plot_dict2={'x':plot_xs2,'y':plot_ys2,'cols':plot_cols2,'colors':plot_colors2}
p2.extra_y_ranges={'margin': Range1d(start=-60, end=210)}
p2.add_layout(LinearAxis(y_range_name="margin",axis_label='Margin between USA and next best team'), 'right')
p2_l1=p2.line(x=plot_dict2['x'][0],y=plot_dict2['y'][0],color='red',legend='USA Points')
p2_l2=p2.line(x=plot_dict2['x'][1],y=plot_dict2['y'][1],color='blue',legend='Margin to 1st',y_range_name='margin')
p2.add_tools(HoverTool(tooltips=[('Points','@y')],mode="vline",renderers=[p2_l1]))
p2.add_tools(HoverTool(tooltips=[('Margin','@y')],mode="vline",renderers=[p2_l2]))
hline = Span(location=0, dimension='width', line_color='black', line_width=0.5, y_range_name="margin",line_dash="dashed")
p2.renderers.extend([hline])
output_file("wnt_rank.html", title="WNT Ranking")

show(gridplot([[p1],[p2]], plot_width=900, plot_height=600))
