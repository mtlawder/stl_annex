################################
#
# US Marathon Trials Analysis
# Author: Matt Lawder
# Date: 11/27/2019
#
################################

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
from os import path
import time
import numpy as np
import re
import datetime
from bokeh.plotting import figure, show, save, output_file
from bokeh.models import ColumnDataSource, HoverTool, DatetimeTickFormatter

scrape_data_fresh=1

print('Starting Trials Analysis')
print('       ---  o         ')
print('        --^/^         ')
print('----------/\----------')
print('----------------------')
bt_hold=time.time()
## Making Folders if necessary
dirpath=f'Trials_Analysis_Output'
if not os.path.exists(dirpath):
    os.mkdir(dirpath)


if scrape_data_fresh==1:
	## GETTING QUALS 04-20, all the pages are slightly different formats, so each one is a little bit custom
	option=['.aspx','/Men-Half-Marathon.aspx','/Women-Marathon.aspx','/Women-Half-Marathon.aspx']
	o_s=['M','M','F','F']
	o_d=['Full','Half','Full','Half']
	all_athlete_df=pd.DataFrame(columns=["Name","Time",'Standard',"Race_w_standard","Rws_location","Rws_date",'Rws_distance',"Sex","Year"])
	j=0
	url_add=['-','']
	for yr in ['2016','2020']:
	    url_plus=url_add[j]
	    url_start=f"http://www.legacy.usatf.org/Events---Calendar/{yr}/U-S--Olympic-Team-Trials---Marathon/Qualifying{url_plus}Standards/Eligible-List"
	    i=0
	    j+=1
	    for url_end in option:
	        main_rep=requests.post(url=url_start+url_end)
	        main_soup=bs(main_rep.text,'html.parser')
	        full_list=main_soup.find_all('tr')
	        record=[]
	        for tr in full_list:
	            row=tr.find_all('td')
	            record+=[[td.text.strip() for td in row]]
	        df=pd.DataFrame.from_records(record[1:-1],columns=["Name","Time",'Standard',"Race_w_standard","Rws_location","Rws_date"])
	        df['Rws_distance']=len(df)*[o_d[i]]
	        df['Sex']=len(df)*[o_s[i]]
	        i+=1
	        df['Year']=len(df)*[int(yr)]
	        all_athlete_df=all_athlete_df.append(df)

	# 2012 had seperate pages for 10k, Half, and Full
	option=['Men/eligible.asp','Men/eligibleByHalfMarathon.asp','Men/eligibleBy10000.asp',\
	        'Women/eligible.asp','Women/eligibleByHalfMarathon.asp','Women/eligibleBy10000.asp']
	o_s=['M','M','M','F','F','F']
	o_d=['Full','Half','10k','Full','Half','10k']
	old_url="http://legacy.usatf.org/events/2012/OlympicTrials-Marathon/entry/entry"
	i=0
	for url_end in option:
	    main_rep=requests.post(url=old_url+url_end)
	    main_soup=bs(main_rep.text,'html.parser')
	    full_list=main_soup.find_all('table',{'class':'blackLines'})[0].find_all('tr')
	    record=[]
	    for tr in full_list:
	        row=tr.find_all('td')
	        record+=[[td.text.strip() for td in row]]
	    df=pd.DataFrame.from_records(record[1:],columns=['Rank','Time','Name','Standard','Race_w_standard','Rws_date','Rws_location'])
	    df['Rws_distance']=len(df)*[o_d[i]]
	    df['Sex']=len(df)*[o_s[i]]
	    i+=1
	    df['Year']=len(df)*[2012]
	    df=df.drop(['Rank'],axis=1)
	    all_athlete_df=all_athlete_df.append(df)

	# Used to determine which event was used to qualify in 08 because all times are listed together
	def qual_event(val):
	    first_digit=val['Time'].split(':')[0]
	    if int(first_digit)==2:
	        return 'Full'
	    elif int(first_digit)==1:
	        return 'Half'
	    else:
	        return '10k'

	for yr in ['2004','2008']:
	    urlw=f"http://legacy.usatf.org/events/{yr}/OlympicTrials-Marathon-Women/entry/status.asp"
	    urlm=f"http://legacy.usatf.org/events/{yr}/OlympicTrials-Marathon-Men/entry/status.asp"
	    o_s=['F','M'] 
	    i=0
	    for url in [urlw,urlm]:  
	        main_rep=requests.post(url=url)
	        main_soup=bs(main_rep.text,'html.parser')
	        full_list=main_soup.find_all('table',{'class':'blackLines'})[0].find_all('tr')
	        # hold_df=all_athlete_df
	        record=[]
	        for tr in full_list:
	            row=tr.find_all('td')
	            record+=[[td.text.strip() for td in row]]
	        df=pd.DataFrame.from_records(record[1:],columns=['Name','Affliation','Time','Entry_status','Dec_status'])
	        df['Rws_distance']=df.apply(qual_event,axis=1)
	        df['Sex']=len(df)*[o_s[i]]
	        i+=1
	        df['Year']=len(df)*[int(yr)]
	        df=df.drop(['Entry_status','Dec_status'],axis=1)
	        all_athlete_df=all_athlete_df.append(df)
	##Removing known asterisks 
	all_athlete_df['Name']=all_athlete_df['Name'].str.replace('*','')
	all_athlete_df['Time']=all_athlete_df['Time'].str.replace('*','')
	all_athlete_df.to_csv('Trials_Analysis_Output/US_Marathon_Trials_Qualifiers_all_years.csv',index=False)
	print('Quals complete')
	print('Time: '+str(time.time()-bt_hold))

	## GETTING RESULTS 00-16, Again slightly different url paths and results formats
	all_athlete_results=pd.DataFrame(columns=['Name','City','HALF_time','FINISH_time','Sex','Year'])
	#The 2016 results were only available in pdf or excel download format, files have been included.
	locations=['2016_womens_us_marathon_trials_results.xlsx','2016_mens_us_marathon_trials_results.xls']
	o_s=['F','M']
	i=0
	for file in locations:
	    results=pd.read_excel(file)
	    results['Sex']=len(results)*[o_s[i]]
	    i+=1
	    results['Year']=len(results)*[2016]
	    results_append=results[['Name','City','HALF_time','FINISH_time','Sex','Year']]
	    all_athlete_results=all_athlete_results.append(results_append)
	# all_athlete_results

	url_ends={'2012':['/results/Men.asp','/results/Women.asp'],'2008':['-Men/results.asp','-Women/results.asp'],\
	          '2004':['-Women/results.asp']}
	tables={'2012':2,'2008':0,'2004':0}
	for yr in ['2008','2012']:
	    o_s=['M','F']
	    i=0
	    for u_end in url_ends[yr]:
	        url_start=f'http://legacy.usatf.org/events/{yr}/OlympicTrials-Marathon'
	                    
	        main_rep=requests.post(url=url_start+u_end)
	        main_soup=bs(main_rep.text,'html.parser')
	        record=[]
	        rows=main_soup.find_all('table')[tables[yr]].find_all('tr')
	        for tr in rows[2:]:
	            row=tr.find_all('td')
	            record+=[[td.text.strip() for td in row]]
	        if yr=='2008':
	            df=pd.DataFrame.from_records(record,columns=['Place','Bib','Name','Age','City','Affliation','FINISH_time'])
	        else:
	            df=pd.DataFrame.from_records(record,columns=['Bib','Name','Age','City','Affliation','FINISH_time','T_diff'])
	        df['Sex']=len(df)*[o_s[i]]
	        i+=1
	        df['Year']=len(df)*[int(yr)]
	        df=df[['Name','Age','City','Affliation','FINISH_time','Sex','Year']]
	        all_athlete_results=all_athlete_results.append(df)

	main_rep=requests.post(url='http://legacy.usatf.org/events/2004/OlympicTrials-Marathon-Women/results.asp')
	main_soup=bs(main_rep.text,'html.parser')
	record=[]
	rows=main_soup.find_all('table')[1].find_all('tr')
	for tr in rows:
	    row=tr.find_all('td')
	    record+=[[td.text.strip() for td in row]]
	df=pd.DataFrame.from_records(record,columns=['Place','Name','Age','City','FINISH_time'])
	df['Sex']=len(df)*['F']
	i+=1
	df['Year']=len(df)*[2004]
	df=df.drop(['Place'],axis=1)
	all_athlete_results=all_athlete_results.append(df)
	# This men's result was just one html string inside a pre tag, no table to parse!
	main_rep=requests.post(url='http://legacy.usatf.org/events/2004/OlympicTrials-Marathon-Men/results.asp')
	main_soup=bs(main_rep.text,'html.parser')
	results=main_soup.find_all('pre')[0].text
	rows=results.split('\r\n')
	record=[row.split() for row in rows[3:-1]]

	result=[[row.strip().split()[0],re.split(r'\s{2,}',row.strip().split(' ',1)[1])[0],\
	 re.split(r'\s{2,}',row.strip().split(' ',1)[1])[1].split(' ',1)[0],\
	#  re.split(r'\s{2,}',row.strip().split(' ',1)[1])[1].split(' ',1)[1],\
	 row.rsplit(' ',1)[1]] for row in rows[3:-1]]
	df=pd.DataFrame.from_records(result,columns=['Place','Name','Age','FINISH_time'])
	df=df.drop(['Place'],axis=1)
	df['Sex']=len(df)*['M']
	df['Year']=len(df)*[2004]
	all_athlete_results=all_athlete_results.append(df)

	main_rep=requests.post(url='http://legacy.usatf.org/events/2000/OlympicTrials-marathon/men/results.asp')
	main_soup=bs(main_rep.text,'html.parser')
	record=[]
	rows=main_soup.find_all('table')[2].find_all('tr')
	for tr in rows:
	    row=tr.find_all('td')
	    record+=[[td.text.strip() for td in row]]
	df=pd.DataFrame.from_records(record,columns=['Place','Name','City_only','State','Age','FINISH_time','Pace'])
	df['Sex']=len(df)*['M']
	i+=1
	df['Year']=len(df)*[2000]
	df['City']=df['City_only']+', '+df['State']
	df=df.drop(['Place','City_only','State','Pace'],axis=1)
	all_athlete_results=all_athlete_results.append(df)

	main_rep=requests.post(url='http://legacy.usatf.org/events/2000/OlympicTrials-marathon/results.asp')
	main_soup=bs(main_rep.text,'html.parser')
	record=[]
	rows=main_soup.find_all('table')[1].find_all('tr')
	for tr in rows:
	    row=tr.find_all('td')
	    record+=[[td.text.strip() for td in row]]
	df=pd.DataFrame.from_records(record,columns=['Place','Name','FINISH_time','City'])
	df['Sex']=len(df)*['F']
	df['Year']=len(df)*[2000]
	df=df.drop(['Place'],axis=1)
	all_athlete_results=all_athlete_results.append(df)
	all_athlete_results.to_csv('Trials_Analysis_Output/US_Marathon_Trials_Results_all_years.csv',index=False)
	print('Results Complete')
	print('Time: '+str(time.time()-bt_hold))
else:
	print('Loading from existing CSVs')

# Reloading csvs
quals=pd.read_csv('Trials_Analysis_Output/US_Marathon_Trials_Qualifiers_all_years.csv'
                  ,encoding='latin')
results=pd.read_csv('Trials_Analysis_Output/US_Marathon_Trials_Results_all_years.csv'
                    ,encoding='latin')

# Setting up a datetime for the times for plotting
def convert_to_dt(val,col):
    if col=='FINISH_time':
        try:
            t=datetime.datetime.strptime(val[col], '%H:%M:%S').time()
        except:
            t=datetime.datetime(2000, 1, 1, 0, 0).time()
    else:
        if val['Rws_distance']=='10k':
            try:
                t=datetime.datetime.strptime(val[col], '%M:%S.%f').time()
            except:
                t=datetime.datetime.strptime(val[col], '%M:%S').time()
        else:
            t=datetime.datetime.strptime(val[col], '%H:%M:%S').time()
    return t
quals['Time']=quals.apply(convert_to_dt,col='Time',axis=1)
results['FINISH_time']=results.apply(convert_to_dt,col='FINISH_time',axis=1)

#Setting unique ID based on name, we do not appear to have name overlap at this point
def name_id(val):
    first_i=val['Name'][0:3]
    yr = val['Year']
    if yr==2012:
        try:
            check = int(val['Name'].split('(')[-1][0])
            return 'Extra'
        except:
            last = val['Name'].split()[-2]
    else:
        last = val['Name'].split()[-1]
    return last+', '+first_i
quals['name_id']=quals.apply(name_id,axis=1)
results['name_id']=results['Name'].str.split().str[-1]+', '+results['Name'].str[0:3]

# Qualifiers by year by sex and by qualifying distance
quals_by_year=quals.groupby(['Year','Sex','Rws_distance']).count().reset_index()[['Year','Sex','Rws_distance','Name']]
quals_by_year['yr_dis']=quals_by_year['Year'].astype('str')+' '+quals_by_year['Rws_distance']
chart=quals_by_year[['yr_dis','Sex','Name']].pivot(index="yr_dis",columns="Sex",values="Name")
chart=chart.reset_index()
## Formatting with place holders in chart for Standard (entered manually)
chart['Year']=chart['yr_dis'].str.split(expand=True)[0]
chart['Distance']=chart['yr_dis'].str.split(expand=True)[1]
chart['M Standard']=len(chart)*['MS']
chart['W Standard']=len(chart)*['WS']
chart['M Qualifiers']=chart['M']
chart['W Qualifiers']=chart['F']
chart[['Year','Distance','M Qualifiers','W Qualifiers','M Standard', 'W Standard']].to_html('Trials_Analysis_Output/quals_chart.html',index=False)

# Merging the Results and Qualifiers to compare how people performed relative to their qualifying mark
qual_to_res=quals.merge(results,on=["name_id","Year"],suffixes=('_qual','_res'))[['name_id','Name_qual','Time','Rws_distance','FINISH_time','Year']]

# all cols with time in total seconds and as a string in addition to dt
def seconds(val):
    try:
        s=val['FINISH_time'].second
        m=val['FINISH_time'].minute*60
        h=val['FINISH_time'].hour*3600
        str_time=val['FINISH_time'].strftime("%H:%M:%S")
        return [s+m+h,str_time]
    except:
        return [0,0]
    
def seconds_qual(val):
    try:
        s=val['Time'].second
        m=val['Time'].minute*60
        h=val['Time'].hour*3600
        str_time=val['Time'].strftime("%H:%M:%S")
        return [int(s+m+h),str_time]
    except:
        return [0,0]

# Getting the qualifier to result difference (useful for Marathon Quals)
def diff_measure(val):
    return (datetime.datetime.combine(datetime.datetime.today(),val['FINISH_time'])-\
        datetime.datetime.combine(datetime.datetime.today(),val['Time'])).seconds

applied_df=pd.DataFrame.from_records(list(qual_to_res.apply(seconds_qual,axis=1)),columns=['fts','qt'])
qual_to_res['fts_qual']=applied_df['fts']
qual_to_res['qual_time']=applied_df['qt']
applied_df=pd.DataFrame.from_records(list(qual_to_res.apply(seconds,axis=1)),columns=['fts','rt'])
qual_to_res['fts']=applied_df['fts']
qual_to_res['result_time']=applied_df['rt']
qual_to_res['diff_time']=qual_to_res.apply(diff_measure,axis=1)

color_look={2016:'red',2012:'blue',2008:'green',2004:'purple',2000:'black'}

    

plotters=qual_to_res.loc[qual_to_res['fts']!=0]
# plotters['color']=plotters.apply(lambda x: 'red' if x['Year']==2016 elif 'blue',axis=1)
plotters['color']=plotters.apply(lambda x: color_look[x['Year']],axis=1)
fig=figure(title="Qualifying Mark vs Actual Result",x_axis_type="datetime",y_axis_type="datetime")
fig2=figure(title="How close did runners come to their Qualifier",x_axis_type="datetime")
d_source=ColumnDataSource({'x':list(plotters['Time']), 'y':list(plotters['FINISH_time']),
            'name':list(plotters['Name_qual']),'qual_time':list(plotters['qual_time']),'finish_time':list(plotters['result_time'])
            ,'color':list(plotters['color']),'year':list(plotters['Year'])})
d_source2=ColumnDataSource({'x':list(plotters['Time']),
            'name':list(plotters['Name_qual']),'qual_time':list(plotters['qual_time']),'finish_time':list(plotters['result_time'])
            ,'color':list(plotters['color']),'year':list(plotters['Year']),'diff':list(plotters['diff_time'])})
p=fig.scatter('x','y',source=d_source,marker='circle',
            line_color="#6666ee", fill_color='color', fill_alpha=0.5, size=12)
p2=fig2.scatter('x','diff',source=d_source2,marker='circle',
            line_color="#6666ee", fill_color='color', fill_alpha=0.5, size=12)
fig.add_tools(HoverTool(tooltips=[("Name", "@name"),("Qualifier", "@qual_time"),('OT Result','@finish_time'),
                                 ('Year','@year')],renderers=[p]))
fig2.add_tools(HoverTool(tooltips=[("Name", "@name"),("Qualifier", "@qual_time"),('OT Result','@finish_time'),
                                 ('Year','@year')],renderers=[p2]))
fig.xaxis.axis_label = 'Qualifying Time'
fig.yaxis.axis_label = 'Olympic Trials Result'
fig2.xaxis.axis_label = 'Qualifying Time'
fig2.yaxis.axis_label = 'Difference between Qualifier and Result (s)'
fig.xaxis.formatter=DatetimeTickFormatter(
        hours=["%H:%M"],
        minutes=["%H:%M"])
fig.yaxis.formatter=DatetimeTickFormatter(
        hours=["%H:%M"],
        minutes=["%H:%M"])
fig2.xaxis.formatter=DatetimeTickFormatter(
        hours=["%H:%M"],
        minutes=["%H:%M"])
output_file('Trials_Analysis_Output/Qualifying_mark_v_Result_time.html')
save(fig)
output_file('Trials_Analysis_Output/Qualifying_mark_v_diff.html')
save(fig2)
print('Quals v Result charts complete')
print('Time: '+str(time.time()-bt_hold))

#Total Qualifiers per year chart
## CREATED TOTAL QUALS PLOT FOR HTML
plot=chart.groupby('Year').agg({'M':np.sum,'F':np.sum}).reset_index()

fig_tq=figure(title="Total Qualifiers by Year",width=500,height=400,tools='reset')
d_source=ColumnDataSource({'x':list(plot['Year']), 'y_w':list(plot['F']),
            'y_m':list(plot['M'])})
p=fig_tq.line('x','y_w',source=d_source,line_color="blue",line_width=4,legend='Women')
p2=fig_tq.line('x','y_m',source=d_source,line_color="red",line_width=4,legend="Men")
fig_tq.add_tools(HoverTool(tooltips=[("Women Qs","@y_w"),("Men Qs", "@y_m"),('Year','@x')],renderers=[p]))
fig_tq.add_tools(HoverTool(tooltips=[("Women Qs","@y_w"),("Men Qs", "@y_m"),('Year','@x')],renderers=[p2]))
# show(fig)
fig_tq.legend.location='top_left'
fig_tq.xaxis.axis_label = 'YEAR'
fig_tq.yaxis.axis_label = 'Qualifiers'
output_file('Trials_Analysis_Output/total_quals_plot.html')
save(fig_tq)

#Looking only at 2020 Qualifiers
quals_20=quals.loc[quals['Year']==2020]
quals_20=quals_20.reset_index()
quals_20.apply(seconds_qual,axis=1)
applied_df=pd.DataFrame.from_records(list(quals_20.apply(seconds_qual,axis=1)),columns=['fts','qt'])
quals_20['fts_qual']=applied_df['fts']
quals_20['qual_time']=applied_df['qt']
plot=quals_20.loc[quals_20['Rws_distance']=='Full']

#Plotting 2020 Qualifiers by time along a line
color_look={'M':'red','F':'blue'}
plot['color']=plot.apply(lambda x: color_look[x['Sex']],axis=1)
fig_ql=figure(title="",width=700,height=100,tools='reset',x_axis_type='datetime')
d_source=ColumnDataSource({'x':list(len(plot)*[0]), 'time':list(plot['Time']),'colors':list(plot['color']),
        'name':list(plot['Name'])})
p=fig_ql.scatter('time','x',source=d_source,marker='circle',
            line_color="colors", fill_color='colors', fill_alpha=0.5, size=8)
fig_ql.add_tools(HoverTool(tooltips=[("Name","@name")],renderers=[p]))
fig_ql.xaxis.axis_label = 'Time'
fig_ql.yaxis.visible = False
fig_ql.yaxis.axis_label = ' '
fig_ql.xaxis.formatter=DatetimeTickFormatter(
        hours=["%H:%M"],
        minutes=["%H:%M"])

output_file('Trials_Analysis_Output/2020_qual_ind.html')
save(fig_ql)

#Plotting 2020 Qualifiers in histogram
hist,edges=np.histogram(list(plot.loc[plot['Sex']=='M']['fts_qual']), bins=26)
hist2,edges2=np.histogram(list(plot.loc[plot['Sex']=='F']['fts_qual']), bins=40)

fig_hist = figure(title='X', tools='', background_fill_color="#fafafa",width=700,height=400)
fig_hist.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="red", line_color="white", alpha=0.5,legend="Men")
fig_hist.quad(top=hist2, bottom=0, left=edges2[:-1], right=edges2[1:],
           fill_color="blue", line_color="white", alpha=0.5,legend="Women")
fig_hist.legend.location='top_left'
fig_hist.yaxis.axis_label='Qualifiers'
fig_hist.xaxis.visible=False
output_file('Trials_Analysis_Output/2020_qual_hist.html')
save(fig_hist)

print('2020 Hist complete')
print('Time: '+str(time.time()-bt_hold))

# From data created basic csv with number of Qualifiers under set time by year
elite=pd.read_csv('elite_quals.csv')

m_e=elite.loc[elite['Sex']=='M']
w_e=elite.loc[elite['Sex']=='F']
plot_m={}
plot_w={}
for t in set(m_e['Under']):
    plot_m[t]=list(m_e.loc[m_e['Under']==t]['Qualifiers'])
for t in set(w_e['Under']):
    plot_w[t]=list(w_e.loc[w_e['Under']==t]['Qualifiers'])
years=[2004,2008,2012,2016,2020]
fig3=figure(title="Women's Elite Qualifiers by Year",width=500,height=400,tools='reset')
fig4=figure(title="Men's Elite Qualifiers by Year",width=500,height=400,tools='reset')
d_source=ColumnDataSource({'x':years, 'w_2:28':plot_w['2:28'],'w_2:30':plot_w['2:30'],'w_2:32':plot_w['2:32']
            ,'w_2:34':plot_w['2:34']})
d_source2=ColumnDataSource({'x':years, 'm_2:10':plot_m['2:10'],'m_2:11':plot_m['2:11'],'m_2:12':plot_m['2:12']
            ,'m_2:13':plot_m['2:13'],'m_2:14':plot_m['2:14']})
w_color=['blue','red','green','black']
m_color=['blue','red','green','black','orange']
i=0
for t in ['2:28', '2:30', '2:32', '2:34']:
    p=fig3.line('x','w_'+t,source=d_source,line_color=w_color[i],line_width=4,legend='Under '+t)
    i+=1
i=0
for t in ['2:10', '2:11', '2:12', '2:13', '2:14']:
    p=fig4.line('x','m_'+t,source=d_source2,line_color=m_color[i],line_width=4,legend='Under '+t)
    i+=1
fig3.legend.location='top_left'
fig4.legend.location='top_left'
fig3.xaxis.axis_label = 'YEAR'
fig3.yaxis.axis_label = 'Qualifiers'
fig4.xaxis.axis_label = 'YEAR'
fig4.yaxis.axis_label = 'Qualifiers'
output_file('Trials_Analysis_Output/women_elite_qual.html')
save(fig3)
output_file('Trials_Analysis_Output/men_elite_qual.html')
save(fig4)

# Repeater Analysis
recent=quals.loc[quals['Year']>2015]
mq=recent.loc[recent['Sex']=='M']
wq=recent.loc[recent['Sex']=='F']
name_ls=mq.groupby('name_id').count().reset_index()
men_repeats=list(name_ls.loc[name_ls['Year']==2]['name_id'])
mq_rep=mq.loc[mq['name_id'].isin(men_repeats)]
name_lsw=wq.groupby('name_id').count().reset_index()
women_repeats=list(name_lsw.loc[name_lsw['Year']==2]['name_id'])
wq_rep=wq.loc[wq['name_id'].isin(women_repeats)]
mq_2016=mq_rep.loc[mq_rep['Year']==2016]
mq_2020=mq_rep.loc[mq_rep['Year']==2020]
m_comp=mq_2016.merge(mq_2020,on="name_id",suffixes=("_2016","_2020"))[['name_id','Name_2016','Rws_distance_2016','Rws_distance_2020']]
wq_2016=wq_rep.loc[wq_rep['Year']==2016]
wq_2020=wq_rep.loc[wq_rep['Year']==2020]
w_comp=wq_2016.merge(wq_2020,on="name_id",suffixes=("_2016","_2020"))[['name_id','Name_2016','Rws_distance_2016','Rws_distance_2020']]
m_comp['Same']=m_comp['Rws_distance_2016']!=m_comp['Rws_distance_2020']
m_comp['2016_Half']=m_comp['Rws_distance_2016']=='Half'
m_comp['Half_to_Full']=m_comp['Same']&m_comp['2016_Half']
w_comp['Same']=w_comp['Rws_distance_2016']!=w_comp['Rws_distance_2020']
w_comp['2016_Half']=w_comp['Rws_distance_2016']=='Half'
w_comp['Half_to_Full']=w_comp['Same']&w_comp['2016_Half']
print('Runners (Men) with a Half QS in 2016 and Full QS in 2020: '+str(len(m_comp.loc[m_comp['Half_to_Full']==True])))
print('Runners (Women) with a Half QS in 2016 and Full QS in 2020: '+str(len(w_comp.loc[w_comp['Half_to_Full']==True])))
print('DONE')