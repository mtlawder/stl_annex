import collections
import pandas as pd
from bokeh.palettes import Category20, Category10
from bokeh.models import HoverTool, LegendItem, Legend
from bokeh.transform import cumsum
from bokeh.layouts import gridplot
from bokeh.embed import components
from bokeh.plotting import ColumnDataSource
from math import pi
from bokeh.plotting import figure
from bokeh.themes import Theme
from bokeh.io import curdoc

def pop_create_table(dd,nbhood,year):
    now_pop=dd.loc[dd['Year']==year]
    now_pop['Black']=now_pop['Black Total'].apply(lambda s: int(s))
    now_pop['White']=now_pop['White Total'].apply(lambda s: int(s))
    if year == 1990:
        now_pop['Other']=now_pop['Other Total'].apply(lambda s: int(s))
        now_pop['Asian']=now_pop['Asian']
        now_pop['Hispanic']=now_pop['Hispanic']
        now_pop['Total']=now_pop['Total Population']
        now_pop['Pacific']=now_pop['Pacific Islander']
        now_pop['Native Am']=now_pop['Native American']
        now_pop['Multi']=now_pop['Two or more']
    else:
        now_pop['Asian']=now_pop['Asian'].apply(lambda s: int(s))
        now_pop['Hispanic']=now_pop['Hispanic'].apply(lambda s: int(s))
        now_pop['Total']=now_pop['Total Population'].apply(lambda s: int(s))
        now_pop['Pacific']=now_pop['Pacific Islander'].apply(lambda s: int(s))
        now_pop['Native Am']=now_pop['Native American'].apply(lambda s: int(s))
        now_pop['Multi']=now_pop['Two or more'].apply(lambda s: int(s))
        now_pop['Other']=now_pop['Other Detail'].apply(lambda s: int(s))
    now_pop_df=now_pop[['Neighborhood','Black','White','Asian','Multi','Pacific','Native Am','Other','Total','Hispanic']]
    now_pop_df=now_pop_df.reset_index()
    now_pop_df=now_pop_df.drop('index',axis=1)
    for col in now_pop_df.columns:
        if col != 'Neighborhood':
            now_pop_df[col+'_pct']=(now_pop_df[col]/now_pop_df['Total'])*100
            now_pop_df[col+'_rank']=now_pop_df[col].rank(method='min',ascending=False)
            now_pop_df[col+'_pct_rank']=now_pop_df[col+'_pct'].rank(method='min',ascending=False)
    selected_df=now_pop_df.loc[now_pop_df['Neighborhood']==nbhood]
    columns=['Total','Black','White','Asian','Multi','Pacific','Native Am','Other','Hispanic']
    cols_dict={'pct':[col+'_pct' for col in columns],'rank':[col+'_rank' for col in columns],'pct_rank':[col+'_pct_rank' for col in columns]}
    x=selected_df[columns].transpose()
    display_df=x.rename(columns={x.columns[0]:'Population'})
    for col in ['rank','pct','pct_rank']:
        x=selected_df[cols_dict[col]].transpose()
        display_df['Pop_'+col]=list(x[x.columns[0]])
    display_df.reset_index(inplace=True,level=0)
    display_df=display_df.rename(columns={'index':'','Pop':'Population','Pop_rank':'Rank','Pop_pct':'Pct','Pop_pct_rank':'Pct Rank'})
    table_data=display_df.to_json(orient='split')
    return table_data


def pop_line_chart(nb,nbhood):
        p2=figure(title="Population of "+nbhood,width=540,height=350,tools='')
        nb['Total_Population']=nb['Total Population']
        nb['Black_Total']=nb['Black Total']
        nb['White_Total']=nb['White Total']
        nb['Other_Total']=nb['Other Total']
        nb=nb.sort_values('Year')
        source=ColumnDataSource(nb)
        color_cnt=0
        legend_p2=[]
        for pop in ['Total_Population','Black_Total','White_Total','Other_Total']:
            if pop=='Total_Population':
                p=p2.line(x='Year',y=pop,source=source,color=Category10[5][2],line_width=3)#,legend={'value':pop})
            else:
                p=p2.line(x='Year',y=pop,source=source,color=Category20[7][color_cnt],line_width=3)#,legend={'value':pop})
                color_cnt+=1
            hover='@'+pop
            p2.add_tools(HoverTool(tooltips=[(str(pop),hover)],renderers=[p]))
            
            legend_p2+=[LegendItem(label=pop[:pop.find('_')],renderers=[p])]
            print(legend_p2)
        p2.add_layout(Legend(items=legend_p2),'right')
        p2.toolbar_location = None
        curdoc().theme=Theme(json={'attrs': {
            'Figure': {
                'background_fill_color':'#edeff2'
            }
            }})
        line_script,line_div=components(p2)
        return line_script,line_div


def pop_pie_chart(nb):
    plots={}
    legend={}
    for yr in [1990,2000,2010]:
        x=collections.OrderedDict()
        if yr == 1990:
            vals=['Black Total','White Total','Other']
            nb['Other']=nb['Other Total']
            single=nb.loc[nb['Year']==yr]
            single=single.reset_index()
            tot=int(single['Total Population'][0])
            for xp in vals:
                x[xp]=int(single[xp][0])
            data=pd.Series(x).reset_index(name='value').rename(columns={'index':'people'})
        else:
            vals=['Black Total','White Total','Other','Asian','Native American','Pacific Islander','Two or more']
            nb['Other']=nb['Other Detail']
            single=nb.loc[nb['Year']==yr]
            single=single.reset_index()
            tot=int(single['Total Population'][0])
            for xp in vals:
                x[xp]=int(single[xp][0])
            data=pd.Series(x).reset_index(name='value').rename(columns={'index':'people'})
        data['angle']=data['value']/data['value'].sum()*2*pi
        data['color']=Category20[len(x)]

        plots[yr]=figure(title="        "+str(yr)+" Pop: "+'{:,}'.format(tot),width=180,height=180,tools='')
        plots[yr].outline_line_color = None
        legend[yr]=plots[yr].wedge(x=0,y=1,radius=0.8,start_angle=cumsum('angle', include_zero=True),\
            end_angle=cumsum('angle'),fill_color='color',line_color='white',source=data)
        plots[yr].axis.axis_label=None
        plots[yr].axis.visible=False
        plots[yr].grid.grid_line_color = None
        plots[yr].background_fill_color = 'white'
        plots[yr].border_fill_color ='white'
        # plot_comb=gridplot([[plots[1990],plots[2000],plots[2010]]])
        # plot_comb.toolbar_location=None
    pie_script,pie_div=components(gridplot([[plots[1990],plots[2000],plots[2010]]],toolbar_options=dict(logo=None)))
    return pie_script,pie_div

def pop_pie_chart_w_legend(nb):
    plots={}
    legend={}
    for yr in [1990,2000,2010]:
        x=collections.OrderedDict()
        if yr == 1990:
            vals=['Black Total','White Total','Other']
            nb['Other']=nb['Other Total']
            single=nb.loc[nb['Year']==yr]
            single=single.reset_index()
            for xp in vals:
                x[xp]=int(single[xp][0])
            data=pd.Series(x).reset_index(name='value').rename(columns={'index':'people'})
        else:
            vals=['Black Total','White Total','Other','Asian','Native American','Pacific Islander','Two or more']
            nb['Other']=nb['Other Detail']
            single=nb.loc[nb['Year']==yr]
            single=single.reset_index()
            for xp in vals:
                x[xp]=int(single[xp][0])
            data=pd.Series(x).reset_index(name='value').rename(columns={'index':'people'})
        data['angle']=data['value']/data['value'].sum()*2*pi
        data['color']=Category20[len(x)]

        if yr==2010:
            plots[yr]=figure(title="Pop "+str(yr),x_range=(-1,3),y_range=(0.2,1.8),width=300,height=190)
            legend[yr]=plots[yr].wedge(x=0.2,y=1,radius=0.9,start_angle=cumsum('angle', include_zero=True),\
                end_angle=cumsum('angle'),fill_color='color',line_color='white',legend='people',source=data)
            plots[yr].legend.label_text_font_size = '8pt'
        else:
            plots[yr]=figure(title="Pop "+str(yr),width=190,height=190)
            legend[yr]=plots[yr].wedge(x=0,y=1,radius=0.7,start_angle=cumsum('angle', include_zero=True),\
                end_angle=cumsum('angle'),fill_color='color',line_color='white',source=data)
        plots[yr].axis.axis_label=None
        plots[yr].axis.visible=False
        plots[yr].grid.grid_line_color = None
        plots[yr].legend.location= 'center_right'
        plots[yr].toolbar_location = None
        plots[yr].background_fill_color = '#edeff2'
    pie_script,pie_div=components(gridplot([[plots[1990],plots[2000],plots[2010]]]))
    return pie_script,pie_div