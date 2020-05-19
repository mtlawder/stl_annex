import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool, FixedTicker, Label, Legend, LegendItem, NumeralTickFormatter
from bokeh.palettes import Category10, Category20

def coronavirus_dashboard_state_charts(state_data):
    state_data['date']=pd.to_datetime(state_data['date'],format="%Y-%m-%d")
    states=['New York','New Jersey','Michigan','Washington','Missouri']
    st_low=state_data.groupby('state').agg({'date':min}).reset_index()
    state_data=state_data.merge(st_low,on='state',how='left',suffixes=('','_start'))
    sd_temp=state_data.loc[state_data['cases']>9]
    st_low2=sd_temp.groupby('state').agg({'date':min}).reset_index()
    state_data=state_data.merge(st_low2,on='state',how='left',suffixes=('','_start_10'))
    state_data['days_since_start']=state_data['date']-state_data['date_start']
    state_data['days_since_start_plot']=state_data.apply(lambda x:
                                        int(str(x['days_since_start']).split(' ')[0]),axis=1)
    state_data['days_since_start_10']=state_data['date']-state_data['date_start_10']
    sbs_df=state_data.loc[state_data['state'].isin(states)]
    sbs_df['days_since_start_10_plot']=sbs_df.apply(lambda x:
                                        int(str(x['days_since_start_10']).split(' ')[0]),axis=1)
    sbs_df=sbs_df.loc[sbs_df['days_since_start_10_plot']>-1]
    p1 = figure(title="Growth after hitting 500 cases",tools=['reset','box_zoom'],height=450,y_range=(0,40000))
    p1.grid.grid_line_alpha=0.4
    p1.xaxis.axis_label = 'Days since 500th case in state'
    p1.yaxis.axis_label = 'Cummulative Cases'
    p1.yaxis.formatter=NumeralTickFormatter(format="0,0")
    color_cnt=0
    p1.border_fill_alpha = 0
    p1.background_fill_color ='#f7f7f7'
    p1.background_fill_alpha = 0.6
    for state in states:
        single_df=sbs_df.loc[state_data['state']==state]
        source=ColumnDataSource(data={'date':list(single_df['date']),'cases':list(single_df['cases']),
                                     'deaths':single_df['deaths'],
                                     'days_since_start_10':single_df['days_since_start_10_plot'],
                                     'date_label':single_df['date'].astype(str)})    
        p=p1.line('days_since_start_10','cases',source=source,color=Category10[10][(color_cnt+6)%10],line_alpha=0.9,
                  line_width=2,legend=state)
        color_cnt+=1
        p1.add_tools(HoverTool(tooltips=[("State",f"{state}"),('Days > 500','@days_since_start_10'),("date",'@date_label'),
                                         ("cases",'@cases{0,}')],renderers=[p],toggleable=False))
    p1.legend.location='top_left'
    comp_st_script,comp_st_div=components(p1)

    avg_growth_df=state_data.loc[state_data['date']>max(state_data['date'])-timedelta(5)]
    avg_growth_df=avg_growth_df.groupby('state').agg({'cases':[max,min]}).reset_index()
    avg_growth_df['pct_diff']=(avg_growth_df['cases']['max']-avg_growth_df['cases']['min'])/avg_growth_df['cases']['min']
    avg_growth_df.columns=avg_growth_df.columns.droplevel(1)
    last_df=state_data.loc[state_data['date']==max(state_data['date'])]
    plot_df=last_df.merge(avg_growth_df[['state','pct_diff']],how='left',on='state')
    p1 = figure(title="Cases v Growth",tools=['reset','box_zoom'],height=450,y_axis_type='log',x_range=(0,200))
    p1.grid.grid_line_alpha=0.4
    p1.border_fill_alpha = 0
    p1.background_fill_color ='#f7f7f7'
    p1.background_fill_alpha = 0.6
    p1.xaxis.axis_label = '5 day growth (%)'
    p1.yaxis.axis_label = 'Cummulative Cases'
    p1.yaxis.formatter=NumeralTickFormatter(format="0,0")
    p1.square([40, 40, 140, 140],[48, 45000, 48, 45000], size=247, color=['#b3ff99','#fff185','#dd99ff','#ff8d85'], alpha=0.5)
    source=ColumnDataSource(data={'cases':plot_df['cases'],'deaths':plot_df['deaths'],
                                     'pct_diff':plot_df['pct_diff']*100,'state':plot_df['state']})    
    p=p1.scatter('pct_diff','cases',source=source,marker='circle',color='blue',size=8,fill_alpha=0.5)
    p1.add_tools(HoverTool(tooltips=[("State","@state"),("Cases",'@cases{0,}'),("5 day chg",'@pct_diff'),
                                    ("Deaths",'@deaths{0,}')],renderers=[p],toggleable=False))
    label_list=[(10,90000,'High Cases'),(10,60000,'Slower Growth'),
               (150,90000,'High Cases'),(150,60000,'Faster Growth'),
               (10,16,'Low Cases'),(10,10,'Slower Growth'),
               (150,16,'Low Cases'),(150,10,'Faster Growth')]
    for dd in label_list:
        mytext = Label(x=dd[0], y=dd[1], text=dd[2],text_font_size ="10pt")
        p1.add_layout(mytext)
    st_script,st_div=components(p1)
    return comp_st_script,comp_st_div,st_script,st_div

def coronavirus_dashboard_charts(state_data):
    state_data['date']=pd.to_datetime(state_data['date'],format="%Y-%m-%d")
    st_low=state_data.groupby('state').agg({'date':min}).reset_index()
    state_data=state_data.merge(st_low,on='state',how='left',suffixes=('','_start'))
    sd_temp=state_data.loc[state_data['cases']>9]
    st_low2=sd_temp.groupby('state').agg({'date':min}).reset_index()
    state_data=state_data.merge(st_low2,on='state',how='left',suffixes=('','_start_10'))
    state_data['days_since_start']=state_data['date']-state_data['date_start']
    state_data['days_since_start_plot']=state_data.apply(lambda x:
                                        int(str(x['days_since_start']).split(' ')[0]),axis=1)
    state_data['days_since_start_10']=state_data['date']-state_data['date_start_10']
    state_data['raw_case_diff']=state_data['cases'].diff()
    state_data['pct_case_diff']=state_data['cases'].pct_change()
    starts=state_data.state != state_data.state.shift(1)
    state_data['raw_case_diff'][starts] = np.nan
    state_data['pct_case_diff'][starts] = np.nan
    p1 = figure(title="Cases by State (Log scale)",x_axis_type='datetime',y_axis_type='log',tools=['reset','box_zoom'],height=450)
    p1.grid.grid_line_alpha=0.4
    p1.grid.grid_line_color='#c2c2c2'
    p1.border_fill_alpha = 0
    p1.background_fill_color ='#f7f7f7'
    p1.background_fill_alpha = 0.6
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Cummulative Cases'
    state_data_sub=state_data.loc[state_data['cases']>499]
    states=set(state_data_sub['state'])
    p1.yaxis.formatter=NumeralTickFormatter(format="0,0")
    color_cnt=0
    p2 = figure(title="Cases by State",tools=['reset','box_zoom'],height=450)
    p2.grid.grid_line_alpha=0.4
    p2.grid.grid_line_color='#c2c2c2'
    p2.xaxis.axis_label = 'Days since first case in state'
    p2.yaxis.axis_label = 'Cummulative Cases'
    p2.border_fill_alpha = 0
    p2.background_fill_color ='#f7f7f7'
    p2.background_fill_alpha = 0.6
    state_data_sub=state_data.loc[state_data['cases']>499]
    states=set(state_data_sub['state'])
    p2.yaxis.formatter=NumeralTickFormatter(format="0,0")
    color_cnt=0
    for state in states:
        single_df=state_data.loc[state_data['state']==state]
        source=ColumnDataSource(data={'date':list(single_df['date']),'cases':list(single_df['cases']),
                                     'deaths':single_df['deaths'],
                                     'days_since_start':single_df['days_since_start_plot'],
                                     'date_label':single_df['date'].astype(str),'pct_diff':single_df['pct_case_diff']})    
        p=p1.line('date','cases',source=source,color=Category20[20][(color_cnt+6)%20],line_alpha=0.9,line_width=2)
        # labels=LabelSet(x='x', y='y', text='names', level='glyph',
        #     x_offset=5, y_offset=5, source=source)
        p1.add_tools(HoverTool(tooltips=[("State",f"{state}"),("date",'@date_label'),
                                         ("cases",'@cases{0,}')],renderers=[p],toggleable=False))
        source=ColumnDataSource(data={'date':list(single_df['date']),'cases':list(single_df['cases']),
                                     'deaths':single_df['deaths'],
                                     'days_since_start':single_df['days_since_start_plot'],
                                     'date_label':single_df['date'].astype(str),'pct_diff':single_df['pct_case_diff']})
        if max(single_df['cases'])>50000:
            if state=='New York':
                labels = Label(x=34, y=100000, text=state)
            else:    
                labels = Label(x=max(single_df['days_since_start_plot'])+0.5, y=max(single_df['cases']), text=state,angle=120)
            p2.add_layout(labels)
        p=p2.line('days_since_start','cases',source=source,color=Category20[20][(color_cnt+6)%20],line_alpha=0.9,line_width=2)
        color_cnt+=1
        p2.add_tools(HoverTool(tooltips=[("State",f"{state}"),("date",'@date_label'),
                                         ("cases",'@cases{0,}')],renderers=[p],toggleable=False))
    cases_log_script,cases_log_div=components(p1)   
    cases_script,cases_div=components(p2)
    return cases_log_script,cases_log_div,cases_script,cases_div