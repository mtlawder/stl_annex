from flask import Flask, render_template, redirect, request, jsonify
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot
from bokeh.embed import components
from bokeh.document import Document
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool, Label, Legend, LegendItem, NumeralTickFormatter, FactorRange
from bokeh.palettes import Category10, Category20
from bokeh.transform import cumsum, dodge
from bokeh.io import curdoc
import holoviews as hv
import panel as pn
import pandas as pd
from static.python.bokeh_plot import pop_pie_chart, pop_line_chart, pop_create_table
from math import pi
import numpy as np
import sqlite3
import datetime
from datetime import datetime,timedelta
import re
import time
from static.python.coronavirus_dashboard import coronavirus_dashboard_state_charts,coronavirus_dashboard_charts,coronavirus_national_charts
from static.python.airlines_in_2020_functions import airline_2020_comp_chart, airline_2020_comp, airlines_in_2020_content
from static.python.airline_project import airline_project_get,airline_project_post
from static.python.passenger_flow_charts import passsenger_flow_all, pie_carrier_plots
hv.extension('bokeh')


app=Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    variable_start_string='<<%',
    variable_end_string='%>>'
))
app.jinja_options = jinja_options

@app.route('/airline_passenger_flow',methods=['GET','POST'])
def airline_passenger_flow():
    if request.method =='GET':
        ap2='LIT'
    else:
        ap2=request.form['airport']
    conn=sqlite3.connect('passenger_flow.db')
    airport_list_df=pd.read_sql('SELECT begin,airport_city,passengers_total FROM route_flow_summary WHERE \
        passengers_total>10000',conn)
    airport_list_df['airport_label']=airport_list_df['begin']+' - '+airport_list_df['airport_city']
    airport_list=airport_list_df[['begin','airport_label']].to_json(orient='split')

    return render_template('/airline_passenger_flow.html',airport_list=airport_list,airport=ap2)

@app.route('/')
def main():
    return redirect('/index_Main')

@app.route('/index_Main',methods=['GET','POST'])
def index_Main():
    return render_template('/index.html')

@app.route('/stl_pop',methods=['GET','POST'])
def stl_pop():
    conn=sqlite3.connect('stl_census.db')
    if request.method =='GET':
        nbhood="Midtown"
        scroll=0
    else:
        nbhood=request.form['nbhoods_send']
        scroll=1
    full_table=pd.read_sql('SELECT * FROM neighborhood_pop',conn)
    neighborhoods=list(set(full_table['Neighborhood']))
    neighborhoods.sort()
    dd=full_table
    nb=dd.loc[dd['Neighborhood']==nbhood]
    # dd=pd.read_sql('SELECT * FROM neighborhood_pop WHERE neighborhood="'+nbhood+'"',conn)
    line_script,line_div=pop_line_chart(nb,nbhood)
    pie_script,pie_div=pop_pie_chart(nb)
    table_data_10=pop_create_table(dd,nbhood,2010)
    table_data_00=pop_create_table(dd,nbhood,2000)
    table_data_90=pop_create_table(dd,nbhood,1990)
    coords_df=pd.read_csv('static/data/STL_neighborhood_lat_lon.csv')
    nb_coords=coords_df.loc[coords_df['Neighborhood']==nbhood]
    coords={'lat':nb_coords.reset_index()['Lat'][0],'lon':nb_coords.reset_index()['Lon'][0]}   
    return render_template('/stl_neighborhood_pop.html',neighbohoods=neighborhoods,line_script=line_script,line_div=line_div,\
        pie_script=pie_script,pie_div=pie_div,table_data_10=table_data_10,table_data_00=table_data_00,\
        table_data_90=table_data_90,nb_sel=nbhood,coords=coords,scroll=scroll)

@app.route('/all_airlines',methods=['GET','POST'])
def all_airlines():
    conn=sqlite3.connect('t_100_segments_forgit.db')
    if request.method =='GET':
        airline_table, air_dest, carriers, dest_options = airline_project_get(conn)
        return render_template('/all_airlines.html',airline_table=airline_table.to_html(classes='table table-striped my-table-all-air', \
            index=False),air_dest=air_dest,var2='ALL',airport_sel='STL',carriers=carriers,carrier_sel='WN', \
            regional_sel='mainline',month_sel=0, year_sel=2018,depart_arrive='depart', show_sel=1,\
            plot_air="",plot_air_script="",dest_options=dest_options)
    else:
        dest_code = request.form['dest_code']
        airport_sel = request.form['airport_sel']
        carrier_sel = request.form['carrier_sel']
        regional_sel = request.form['regional_sel']
        month_sel = request.form['month_value']
        year_sel = request.form['year_value']
        depart_arrive = request.form['depart_arrive']
        total_df,air_dest,carriers,div,script,dest_options=airline_project_post(dest_code,airport_sel,carrier_sel,regional_sel,month_sel,year_sel,depart_arrive,conn)
        return render_template('/all_airlines.html',airline_table=total_df.to_html(classes='table table-striped my-table-all-air',index=False)\
            ,air_dest=air_dest,var2=dest_code,airport_sel=airport_sel,carriers=carriers,carrier_sel=carrier_sel,regional_sel=regional_sel,month_sel=month_sel,\
            year_sel=year_sel,depart_arrive=depart_arrive,plot_air=div,show_sel=0, \
            plot_air_script=script,dest_options=dest_options)        

@app.route('/airlines',methods=['GET','POST'])
def airlines():
    conn=sqlite3.connect('airport.db')
    if request.method =='GET':
        airlines=pd.read_sql('SELECT * FROM stl_airport WHERE Datetime>="2017-07-13T00:00:00" AND Datetime<="2017-07-14T00:00:00" ORDER BY Destination' ,conn)
        airlines[['Airline_only','flight_number']]=airlines.Airline.str.split(' #',expand=True)
        airlines['Airline_only']=airlines['Airline_only'].str.strip()
        airline_table=airlines[['Airline_only','flight_number']].groupby('Airline_only').agg([len])
        airline_table.columns=['flights']
        airline_table.reset_index(inplace=True)
        airs=airlines['Airline_only'].drop_duplicates()
        return render_template('/airlines.html', airline_table=airline_table.to_html(classes='table table-striped',index=False),airs=airs)
    else:
        destination=request.form['destination']
        date=request.form['date']
        try:
            date_x=datetime.strptime(date,'%Y-%m-%d').strftime('%m/%d/%Y')
            date_y=datetime.strptime(date,'%Y-%m-%d').strftime('%Y-%m-%d')+'T01:00:00'
            date_z=(datetime.strptime(date,'%Y-%m-%d')-timedelta(days=1)).strftime('%Y-%m-%d')+'T01:00:00'
            sample_table=pd.read_sql('SELECT * FROM stl_airport WHERE Destination="%s" and Date="%s"' %(destination,date_x),conn)
            airlines=pd.read_sql('SELECT * FROM stl_airport WHERE Datetime>="%s" AND Datetime<="%s"  ORDER BY Destination' %(date_z,date_y),conn)
            airlines[['Airline_only','flight_number']]=airlines.Airline.str.split(' #',expand=True)
            airlines['Airline_only']=airlines['Airline_only'].str.strip()
            airline_table=airlines[['Airline_only','flight_number']].groupby('Airline_only').agg([len])
            airline_table.columns=['flights']
            airline_table.reset_index(inplace=True)
            return render_template('/airlines.html', table=sample_table.to_html(classes='table table-striped',index=False), airline_table=airline_table.to_html(classes='table table-striped',index=False), date_look=date_x)
        except:
            try:
                sample_table=pd.read_sql('SELECT * FROM stl_airport WHERE Destination="%s"' %(destination),conn)
                return render_template('/airlines.html', table=sample_table.to_html(classes='table table-striped',index=False), date_look=date)
            except:
                return render_template('/airlines.html',table="Need to choose proper destination",date="No date choosen")

@app.route('/airlines_types',methods=['GET','POST'])
def airline_types():
    conn=sqlite3.connect('airport.db')
    destination=request.form['airline_type']
    date=request.form['date']
    try:
        date_x=datetime.strptime(date,'%Y-%m-%d').strftime('%m/%d/%Y')
        date_y=datetime.strptime(date,'%Y-%m-%d').strftime('%Y-%m-%d')+'T01:00:00'
        date_z=(datetime.strptime(date,'%Y-%m-%d')-timedelta(days=1)).strftime('%Y-%m-%d')+'T01:00:00'
        print(destination)
        print(date_x)
        return render_template('/airlines.html', table="S", airline_table="s", date_look=date_x)
    except:
        return render_template('/airlines.html',table="Need to choose proper destination!",date="No date choosen")

@app.route('/coronavirus_dashboard',methods=['GET','POST'])
def coronavirus_dashboard():
    state_data=pd.read_csv('static/data/us-states.csv')
    today_vals,national_div,national_script,national_log_div,national_log_script=coronavirus_national_charts(state_data)
    return render_template('/coronavirus_dashboard.html',today_vals=today_vals,national_div=national_div,national_script=national_script,
        national_log_div=national_log_div,national_log_script=national_log_script)

@app.route('/blogs_2021/<blog_title>',methods=['GET','POST'])
def blog2021(blog_title):
    return render_template(f'/blogs_2021/{blog_title}.html')

@app.route('/blogs_2020/<blog_title>',methods=['GET','POST'])
def blog2020(blog_title):
    return render_template(f'/blogs_2020/{blog_title}.html')

@app.route('/blogs_2019/<blog_title>',methods=['GET','POST'])
def blog2019(blog_title):
    return render_template(f'/blogs_2019/{blog_title}.html')   

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('/about.html')

@app.route('/<airline>_stl_by_the_numbers',methods=['GET','POST'])
def stl_by_the_numbers(airline):
    return render_template(f'/by_the_numbers/{airline}_STL_btn.html')

@app.route('/allegiant_blv_by_the_numbers',methods=['GET','POST'])
def allegiant_blv_by_the_numbers():
    return render_template('/by_the_numbers/allegiant_BLV_btn.html')

@app.route('/southwest_stl_BIG',methods=['GET','POST'])
def southwest_stl_BIG():
    return render_template('/by_the_numbers/STL_WN_BIG_charts_all.html')

@app.route('/btn_methodology',methods=['GET','POST'])
def btn_methodology():
    return render_template('/by_the_numbers/btn_methodology.html')

@app.route('/all_stl_nbh_census',methods=['GET','POST'])
def all_stl_nbh_census():
    return render_template('/all_stl_census_neighborhoods.html')

@app.route('/blog_marathon_times_yoy',methods=['GET','POST'])
def blog_marathon_times_yoy():
    return render_template('/blog_marathon_times_yoy.html')

@app.route('/blog_cptc_results',methods=['GET','POST'])
def blog_cptc_results():
    return render_template('/running/blog_cptc_results.html')

@app.route('/amtrak_timeline_scroll',methods=['GET','POST'])
def amtrak_timeline_scroll():
    return render_template('/amtrak_timeline_scroll.html')


@app.route('/airlines_in_2020',methods=['GET','POST'])
def airlines_in_2020():
    if request.method =='GET':
        air_sel='STL'
    else:
        air_sel=request.form['airport']
    totals_display,pass_script,pass_div,dept_script,dept_div,seats_script,seats_div,airport_list,routes_display, latest_month_label=airlines_in_2020_content(air_sel)
    return render_template('/airlines_in_2020.html',air_sel=air_sel,totals_display=totals_display,pass_script=pass_script,pass_div=pass_div,
        dept_script=dept_script,dept_div=dept_div,seats_script=seats_script,seats_div=seats_div,
        airport_list=airport_list,routes_display=routes_display, latest_month_label= latest_month_label)

@app.route('/all_blogs',methods=['GET','POST'])
def all_blogs():
    return render_template('/all_blogs.html')

### API CALLS ###

@app.route('/api/airline_2020_comp',methods=['GET','POST'])
def api_airlines_2020_comp():
    airport = request.form["airport"]
    send_df = airline_2020_comp(airport)
    return send_df.to_json(orient='index')

@app.route('/api/airline_2020_comp_chart',methods=['GET','POST'])
def api_airlines_2020_comp_chart():
    airports = request.form["airports"].split(',')
    airport_comp_script,airport_comp_div=airline_2020_comp_chart(airports)
    return jsonify({'airport_comp_script':airport_comp_script,'airport_comp_div':airport_comp_div})

@app.route('/api/blog_return',methods=['POST'])
def api_blog_return():
    total_post = request.form["totalPosts"]
    conn=sqlite3.connect("website_meta.db")
    sql_command="SELECT URL, Title, StartDate, Author, RawSummary From blogs_meta ORDER BY ID DESC"
    if total_post != 'all':
        sql_command+=f" LIMIT {total_post}"
    blogs=pd.read_sql(sql_command,conn).to_json(orient='records')
    return blogs

@app.route('/api/nieghbhoor_pop_data',methods=['POST'])
def api_nieghbhoor_pop_data():
    conn=sqlite3.connect('stl_census.db')
    nbhood=request.form['nbhoods_send']
    full_table=pd.read_sql('SELECT * FROM neighborhood_pop',conn)
    dd=full_table
    nb=dd.loc[dd['Neighborhood']==nbhood]
    line_script,line_div=pop_line_chart(nb,nbhood)
    pie_script,pie_div=pop_pie_chart(nb)
    table_data_10=pop_create_table(dd,nbhood,2010)
    table_data_00=pop_create_table(dd,nbhood,2000)
    table_data_90=pop_create_table(dd,nbhood,1990)
    coords_df=pd.read_csv('static/data/STL_neighborhood_lat_lon.csv')
    nb_coords=coords_df.loc[coords_df['Neighborhood']==nbhood]
    coords={'lat':nb_coords.reset_index()['Lat'][0],'lon':nb_coords.reset_index()['Lon'][0]}
    return jsonify({'table_data_10':table_data_10,'table_data_00':table_data_00,'table_data_90':table_data_90,'coords':coords,\
        'line_script':line_script,'line_div':line_div,'pie_script':pie_script,'pie_div':pie_div})

@app.route('/api/state_comp',methods=['GET','POST'])
def api_state_comp():
    state_data=pd.read_csv('static/data/us-states.csv')
    comp_st_script,comp_st_div,st_script,st_div=coronavirus_dashboard_state_charts(state_data)
    return jsonify({'comp_st_script':comp_st_script,'comp_st_div':comp_st_div,'st_script':st_script,'st_div':st_div})

@app.route('/api/states',methods=['GET','POST'])
def api_states():
    state_data=pd.read_csv('static/data/us-states.csv')
    cases_log_script,cases_log_div,cases_script,cases_div=coronavirus_dashboard_charts(state_data)
    return jsonify({'cases_script':cases_script,'cases_div':cases_div,'cases_log_script':cases_log_script,'cases_log_div':cases_log_div})

@app.route('/api/passenger_flow',methods=['GET','POST'])
def passenger_flow():
    ap2 = request.form["airport"]
    reg = request.form["reg_main_select"]
    advanced = request.form["advanced"]
    car = request.form["carrier_select"]
    div,script,div_t100,script_t100,div_pie,script_pie,table_data,total_pass,od_pass,route_pass_end,t100_data,valid_data=passsenger_flow_all(ap2,reg,advanced,car)
    return jsonify({'sankeychartscript':script,'sankeychartdiv':div,'table_data':table_data,'total_pass':total_pass,'t100_data':t100_data,
        'script_t100':script_t100,'div_t100':div_t100,'script_pie':script_pie,'div_pie':div_pie,'valid_data':valid_data,'od_pass':od_pass,
        'route_pass_end':route_pass_end})

@app.route('/api/passenger_flow_pie_carrier_only',methods=['GET','POST'])
def passenger_flow_pie_carrier_only():
    ap2 = request.form["airport"]
    reg = request.form["reg_main_select"]
    advanced = request.form["advanced"]
    car = request.form["carrier_select"]
    div_pie,script_pie=pie_carrier_plots(ap2,reg,advanced,car)
    return jsonify({'script_pie':script_pie,'div_pie':div_pie})

if __name__ == '__main__':
    app.run()


