from flask import Flask, render_template, redirect, request, jsonify
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot
from bokeh.embed import components
from bokeh.document import Document
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool, Label, Legend, LegendItem, NumeralTickFormatter, FactorRange
from bokeh.palettes import Category10, Category20
from bokeh.transform import cumsum, dodge
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



app=Flask(__name__)

jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    variable_start_string='<<%',
    variable_end_string='%>>'
))
app.jinja_options = jinja_options

@app.route('/')
def main():
    return redirect('/index_Main')

@app.route('/index_Main',methods=['GET','POST'])
def index_Main():
    return render_template('/index.html')

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

@app.route('/stl_pop',methods=['GET','POST'])
def stl_pop():
    conn=sqlite3.connect('stl_census.db')
    if request.method =='GET':
        full_table=pd.read_sql('SELECT * FROM neighborhood_pop',conn)
        neighborhoods=list(set(full_table['Neighborhood']))
        neighborhoods.sort()
        nbhood="Midtown"
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
        #Creating data table to send
                
        return render_template('/stl_neighborhood_pop.html',neighbohoods=neighborhoods,line_script=line_script,line_div=line_div,\
            pie_script=pie_script,pie_div=pie_div,table_data_10=table_data_10,table_data_00=table_data_00,\
            table_data_90=table_data_90,nb_sel=nbhood,coords=coords,scroll=0)
    else:
        nbhood=request.form['nbhoods_send']
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
        # table_data={'columns':[],'data':{}}
        # nbh_table=pd.read_sql('SELECT * FROM neighborhood_pop WHERE neighborhood="%s"' %(neighborhood), conn)
        # p1 = figure(title="Population Change")
        # p1.line(pd.to_numeric(nbh_table['Year']), pd.to_numeric(nbh_table['Total Population'].str.replace(',','')))
        # script, div = components(p1)
        return render_template('/stl_neighborhood_pop.html',neighbohoods=neighborhoods,line_script=line_script,line_div=line_div,\
            pie_script=pie_script,pie_div=pie_div,table_data_10=table_data_10,table_data_00=table_data_00,\
            table_data_90=table_data_90,nb_sel=nbhood,coords=coords,scroll=1)

@app.route('/all_airlines',methods=['GET','POST'])
def all_airlines():
    conn=sqlite3.connect('t_100_segments_forgit.db')
    if request.method =='GET':
        d_ops=pd.read_sql('SELECT ORIGIN, DEST, PASSENGERS FROM domestic_routes\
          WHERE (ORIGIN IN ("STL","IND","DSM","MCI","MEM","CVG","SBN","COU","SGF")) AND PASSENGERS>100 GROUP BY ORIGIN, DEST', conn)
        dest_options={city: list(d_ops[d_ops["ORIGIN"]==city]["DEST"]) for city in ["STL","IND","DSM","MCI","MEM","CVG","SBN","COU","SGF"]}
        carrier = "WN"
        # airline_table=pd.read_sql(f'SELECT SUM(DEPARTURES_PERFORMED) AS DEPARTURES,SUM(SEATS) AS "TOTAL CAPACITY",SUM(PASSENGERS)\
        #     AS "TOTAL PASSENGERS", UNIQUE_CARRIER_NAME, DEST, DEST_CITY_NAME,YEAR FROM domestic_routes\
        #     WHERE ORIGIN="STL" AND YEAR=2017 AND UNIQUE_CARRIER="{carrier}" GROUP BY DEST,UNIQUE_CARRIER ORDER BY "TOTAL PASSENGERS" DESC', conn)
        airline_table=pd.read_sql(f'SELECT SUM(DEPARTURES_PERFORMED) AS DEPARTURES,SUM(SEATS) AS "TOTAL CAPACITY",SUM(PASSENGERS) \
            AS "TOTAL PASSENGERS",UNIQUE_CARRIER_NAME,DEST,DEST_CITY_NAME,YEAR,ORIGIN,ORIGIN_CITY_NAME FROM domestic_routes WHERE ORIGIN="STL" AND YEAR="2018" AND UNIQUE_CARRIER="{carrier}"\
            GROUP BY DEST,UNIQUE_CARRIER ORDER BY "TOTAL PASSENGERS" DESC',conn)
        airline_table=airline_table.loc[airline_table["TOTAL PASSENGERS"]>100]
        airline_table['LOAD FACTOR']=(airline_table['TOTAL PASSENGERS']/airline_table['TOTAL CAPACITY'])*100
        airline_table['LOAD FACTOR']=airline_table['LOAD FACTOR'].map('{:,.1f}%'.format)
        cols=airline_table.columns.tolist()
        airline_table=airline_table[cols[:3]+['LOAD FACTOR']+cols[3:-1]]
        air_dest = airline_table.values.tolist()
        carriers = list(set(airline_table["UNIQUE_CARRIER_NAME"].tolist()))
        print(carriers)
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
        month_insert =""
        carrier_insert =""
        dest_insert=""
        combined_insert = ""
        join_insert=""
        #combined_org_insert=""
        cols_insert="A.DEST, DEST_CITY_NAME"
        groupby_insert="A.DEST"
        origin_insert=f'A.ORIGIN="{airport_sel}"'
        year_insert="AND A.YEAR=2017"
        if month_sel!='0':
            month_insert="AND A.MONTH="+str(month_sel)
        if carrier_sel!='ALL' and carrier_sel!='ALL_SELECTED':
            carrier_insert='AND A.UNIQUE_CARRIER="'+str(carrier_sel)+'"'
        if depart_arrive == 'depart':
            join_insert="A.ORIGIN=B.origin AND A.DEST=B.destination"
            if dest_code!='' and dest_code!='ALL':
                dest_insert='AND A.DEST="'+str(dest_code)+'"'
        elif depart_arrive == 'arrive':
            join_insert="A.ORIGIN=B.destination AND A.DEST=B.origin"
            if dest_code!='' and dest_code!='ALL':
                dest_insert='AND A.ORIGIN="'+str(dest_code)+'"'
            origin_insert=f'A.DEST="{airport_sel}"'
            cols_insert="A.ORIGIN AS DEST, ORIGIN_CITY_NAME AS DEST_CITY_NAME"
            groupby_insert="A.ORIGIN"
        else:
            pass
        #    if dest_code!='' and dest_code!='ALL':
        #        dest_insert='AND A.DEST="'+str(dest_code)+'"'
        #        combined_org_insert='AND A.ORIGIN="'+str(dest_code)+'"'
        #    combined_insert=f'OR (A.DEST="{airport_sel}" {combined_org_insert} {year_insert} {carrier_insert} {month_insert})'
        if year_sel=='All':
            year_insert=""
        else:
            year_insert='AND A.YEAR="'+str(year_sel)+'"'
            print(origin_insert,year_insert,dest_insert,carrier_insert,month_insert,combined_insert,groupby_insert,cols_insert)
        d_ops=pd.read_sql('SELECT ORIGIN, DEST, PASSENGERS FROM domestic_routes\
          WHERE (ORIGIN IN ("STL","IND","DSM","MCI","MEM","CVG","SBN","COU","SGF")) AND PASSENGERS>100 GROUP BY ORIGIN, DEST', conn)
        dest_options={city: list(d_ops[d_ops["ORIGIN"]==city]["DEST"]) for city in ["STL","IND","DSM","MCI","MEM","CVG","SBN","COU","SGF"]}
        if regional_sel=='mainline':
            # airline_table=pd.read_sql(f'SELECT SUM(DEPARTURES) AS DEPARTURES,SUM("TOTAL CAPACITY") AS "TOTAL CAPACITY",SUM("TOTAL PASSENGERS") \
            #     AS "TOTAL PASSENGERS", UNIQUE_CN AS UNIQUE_CARRIER_NAME, DEST, DEST_CITY_NAME,YEAR FROM \
            #     (SELECT SUM(DEPARTURES_PERFORMED) AS DEPARTURES,SUM(SEATS) AS "TOTAL CAPACITY",SUM(PASSENGERS) \
            #     AS "TOTAL PASSENGERS", COALESCE(mainline_desc,UNIQUE_CARRIER_NAME) AS UNIQUE_CN, \
            #     {cols_insert},A.YEAR FROM domestic_routes AS A LEFT JOIN regional_conversion as B \
            #     ON {join_insert} AND A.UNIQUE_CARRIER=B.regional_code AND A.YEAR=B.year WHERE \
            #     ({origin_insert} {year_insert} {dest_insert} {carrier_insert} {month_insert}) {combined_insert} GROUP BY {groupby_insert}, \
            #     UNIQUE_CARRIER_NAME) AS COMB GROUP BY DEST,UNIQUE_CARRIER_NAME ORDER BY "TOTAL PASSENGERS" DESC', conn)
            airline_table=pd.read_sql(f'SELECT SUM(DEPT_ADJ) AS DEPARTURES,SUM(SEATS_ADJ) AS "TOTAL CAPACITY",SUM(PASS_ADJ) AS "TOTAL PASSENGERS",B.UNIQUE_CARRIER_NAME,\
                DEST,DEST_CITY_NAME,YEAR,ORIGIN,ORIGIN_CITY_NAME FROM domestic_routes AS A LEFT JOIN carrier_mapping AS B ON A.MAIN_CARRIER=B.UNIQUE_CARRIER \
                WHERE ({origin_insert} {year_insert} {dest_insert} {carrier_insert} {month_insert}) {combined_insert} \
                GROUP BY {groupby_insert},MAIN_CARRIER ORDER BY "TOTAL PASSENGERS" DESC', conn)
        else:
            # airline_table=pd.read_sql(f'SELECT SUM(DEPARTURES_PERFORMED) AS DEPARTURES,SUM(SEATS) AS "TOTAL CAPACITY",SUM(PASSENGERS) \
            #     AS "TOTAL PASSENGERS", UNIQUE_CARRIER_NAME, \
            #     {cols_insert},A.YEAR FROM domestic_routes AS A LEFT JOIN regional_conversion as B \
            #     ON {join_insert} AND A.UNIQUE_CARRIER=B.regional_code AND A.YEAR=B.year WHERE \
            #     ({origin_insert} {year_insert} {dest_insert} {carrier_insert} {month_insert}) {combined_insert} GROUP BY {groupby_insert},UNIQUE_CARRIER_NAME ORDER BY "TOTAL PASSENGERS" DESC', conn)
            airline_table=pd.read_sql(f'SELECT SUM(DEPT_ADJ) AS DEPARTURES,SUM(SEATS_ADJ) AS "TOTAL CAPACITY",SUM(PASS_ADJ) AS "TOTAL PASSENGERS",UNIQUE_CARRIER_NAME,\
                DEST,DEST_CITY_NAME,YEAR,ORIGIN,ORIGIN_CITY_NAME FROM domestic_routes AS A WHERE ({origin_insert} {year_insert} {dest_insert} {carrier_insert} {month_insert}) {combined_insert} \
                GROUP BY {groupby_insert},UNIQUE_CARRIER_NAME ORDER BY "TOTAL PASSENGERS" DESC', conn)
        airline_table=airline_table.loc[airline_table["TOTAL PASSENGERS"]>100]
        airline_table['LOAD FACTOR']=(airline_table['TOTAL PASSENGERS']/airline_table['TOTAL CAPACITY'])*100
        airline_table['LOAD FACTOR']=airline_table['LOAD FACTOR'].map('{:,.1f}%'.format)
        airline_table=airline_table.round({'DEPARTURES':0,'TOTAL CAPACITY':0,'TOTAL PASSENGERS':0})


        total_df=pd.DataFrame(columns=['DEPARTURES','TOTAL CAPACITY','TOTAL PASSENGERS','LOAD FACTOR',\
        'UNIQUE_CARRIER_NAME','DEST','DEST_CITY_NAME','YEAR','ORIGIN','ORIGIN_CITY_NAME'\
        ],data=[[airline_table["DEPARTURES"].sum(),airline_table["TOTAL CAPACITY"].sum(),airline_table["TOTAL PASSENGERS"].sum(),\
        (airline_table["TOTAL PASSENGERS"].sum()/airline_table["TOTAL CAPACITY"].sum())*100 if airline_table["TOTAL CAPACITY"].sum()!=0 else 0\
        ,"ALL SELECTED","ALL","ALL",year_sel,"ALL","ALL"]])
        total_df["LOAD FACTOR"]=total_df["LOAD FACTOR"].map('{:,.1f}%'.format)
        cols=airline_table.columns.tolist()
        airline_table=airline_table[cols[:3]+['LOAD FACTOR']+cols[3:-1]]
        total_df=total_df.append(airline_table)
        carriers = list(set(total_df["UNIQUE_CARRIER_NAME"].tolist()))
        #carriers='a'
        air_dest = total_df.values.tolist()
        script=""
        div=""
        if dest_code!='' and dest_code!='ALL':
            p_air_tab=pd.read_sql(f'SELECT SUM(PASSENGERS) AS PASS, YEAR, MONTH FROM domestic_routes AS A WHERE {origin_insert} \
            {dest_insert} {carrier_insert} GROUP BY YEAR, MONTH', conn)
            #p1 = figure(title="Airline Passengers")
            #p1.line(pd.to_numeric(p_air_tab['YEAR']+(p_air_tab['MONTH']-1)/12), pd.to_numeric(p_air_tab['PASS']))
            p1 = figure(x_range=list(p_air_tab['YEAR'].astype(str)+'-'+p_air_tab['MONTH'].astype(str)), plot_height=250,
                plot_width=700,title="Passenger Counts all Carriers", toolbar_location=None, tools="")
            d_source=ColumnDataSource({'x':list(p_air_tab['YEAR'].astype(str)+'-'+p_air_tab['MONTH'].astype(str)),
                           'y':list(p_air_tab['PASS']/1000)})
            p=p1.vbar(x='x', top='y', source=d_source, width=0.85)
            p1.add_tools(HoverTool(tooltips=[("Yr-Mo",'@x'),("Passengers", "@y{,0}k")],renderers=[p]))
            p1.xgrid.grid_line_color = None
            p1.y_range.start = 0
            p1.xaxis.major_label_orientation = 1.2
            p1.yaxis.axis_label= "Thousands of Passengers"
            script, div = components(p1)
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
        #sample_table=pd.read_sql('SELECT * FROM stl_airport WHERE (Airline LIKE "%Air Canada%") and Date="%s"' %(destination,date_x),conn)
        #airlines=pd.read_sql('SELECT * FROM stl_airport WHERE Datetime>="%s" AND Datetime<="%s"  ORDER BY Destination' %(date_z,date_y),conn)
        print(date_x)
        #airlines[['Airline_only','flight_number']]=airlines.Airline.str.split(' #',expand=True)
        #airlines['Airline_only']=airlines['Airline_only'].str.strip()
        #airline_table=airlines[['Airline_only','flight_number']].groupby('Airline_only').agg([len])
        #airline_table.columns=['flights']
        #airline_table.reset_index(inplace=True)
        #return render_template('/airlines.html', table=sample_table.to_html(classes='table table-striped',index=False), airline_table=airline_table.to_html(classes='table table-striped',index=False), date_look=date_x)
        return render_template('/airlines.html', table="S", airline_table="s", date_look=date_x)
    except:
        return render_template('/airlines.html',table="Need to choose proper destination!",date="No date choosen")

@app.route('/coronavirus_dashboard',methods=['GET','POST'])
def coronavirus_dashboard():
    state_data=pd.read_csv('static/data/us-states.csv')
    today_vals,national_div,national_script,national_log_div,national_log_script=coronavirus_national_charts(state_data)
    return render_template('/coronavirus_dashboard.html',today_vals=today_vals,national_div=national_div,national_script=national_script,
        national_log_div=national_log_div,national_log_script=national_log_script)

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

@app.route('/blog_starting_airline_route_post',methods=['GET','POST'])
def blog_starting_airline_route_post():
    return render_template('/blog_starting_airline_route_post.html')

@app.route('/blog_load_factors_from_STL',methods=['GET','POST'])
def blog_load_factors_from_stl():
    return render_template('/blog_load_factors_from_STL.html')

@app.route('/blog_uswnt_ranking',methods=['GET','POST'])
def blog_uswnt_ranking():
    return render_template('/blog_uswnt_ranking.html')

@app.route('/blog_southwest_5yr_growth_STL',methods=['GET','POST'])
def blog_southwest_5yr_growth_STL():
    return render_template('/blog_southwest_5yr_growth_STL.html')

@app.route('/blog_od_pairs_STL',methods=['GET','POST'])
def blog_od_pairs_STL():
    return render_template('/blog_od_pairs_STL.html')

@app.route('/blog_Southwest_out_of_Newark',methods=['GET','POST'])
def blog_Southwest_out_of_Newark():
    return render_template('/blog_Southwest_out_of_Newark.html')

@app.route('/blog_southwest_ewr_lga_comp',methods=['GET','POST'])
def blog_southwest_ewr_lga_comp():
    return render_template('/blog_southwest_ewr_lga_comp.html')    

@app.route('/blog_first_stl_pop',methods=['GET','POST'])
def blog_first_stl_pop():
    return render_template('/blog_first_stl_pop.html')    

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('/about.html')

@app.route('/delta_stl_by_the_numbers',methods=['GET','POST'])
def delta_stl_by_the_numbers():
    return render_template('/by_the_numbers/delta_STL_btn.html')

@app.route('/frontier_stl_by_the_numbers',methods=['GET','POST'])
def frontier_stl_by_the_numbers():
    return render_template('/by_the_numbers/frontier_STL_btn.html')

@app.route('/united_stl_by_the_numbers',methods=['GET','POST'])
def united_stl_by_the_numbers():
    return render_template('/by_the_numbers/united_STL_btn.html')

@app.route('/allegiant_blv_by_the_numbers',methods=['GET','POST'])
def allegiant_blv_by_the_numbers():
    return render_template('/by_the_numbers/allegiant_BLV_btn.html')

@app.route('/american_stl_by_the_numbers',methods=['GET','POST'])
def american_stl_by_the_numbers():
    return render_template('/by_the_numbers/american_STL_btn.html')

@app.route('/airchoiceone_stl_by_the_numbers',methods=['GET','POST'])
def airchoiceone_stl_by_the_numbers():
    return render_template('/by_the_numbers/airchoiceone_STL_btn.html')

@app.route('/alaska_stl_by_the_numbers',methods=['GET','POST'])
def alaska_stl_by_the_numbers():
    return render_template('/by_the_numbers/alaska_STL_btn.html')

@app.route('/southwest_stl_by_the_numbers',methods=['GET','POST'])
def southwest_stl_by_the_numbers():
    return render_template('/by_the_numbers/southwest_STL_btn.html')

@app.route('/southwest_stl_BIG',methods=['GET','POST'])
def southwest_stl_BIG():
    return render_template('/by_the_numbers/STL_WN_BIG_charts_all.html')

@app.route('/btn_methodology',methods=['GET','POST'])
def btn_methodology():
    return render_template('/by_the_numbers/btn_methodology.html')

@app.route('/blog_us_marathon_trials_2020',methods=['GET','POST'])
def blog_us_marathon_trials_2020():
    return render_template('/blog_us_marathon_trials_2020.html')

@app.route('/blog_us_marathon_trials_2020_p2',methods=['GET','POST'])
def blog_us_marathon_trials_2020_p2():
    return render_template('/blog_us_marathon_trials_2020_p2.html')

@app.route('/all_stl_nbh_census',methods=['GET','POST'])
def all_stl_nbh_census():
    return render_template('/all_stl_census_neighborhoods.html')

@app.route('/connecting_airport_traffic',methods=['GET','POST'])
def connecting_airport_traffic():
    return render_template('/blog_airport_connections.html')

@app.route('/blog_od_ranks',methods=['GET','POST'])
def blog_od_ranks():
    return render_template('/blog_od_ranks.html')

@app.route('/blog_nyc_airports_od_comp',methods=['GET','POST'])
def blog_nyc_airports_od_comp():
    return render_template('/blog_nyc_airports_od_comp.html')

@app.route('/blog_stl_od',methods=['GET','POST'])
def blog_stl_od():
    return render_template('/blog_stl_od.html')

@app.route('/blog_marathon_times_yoy',methods=['GET','POST'])
def blog_marathon_times_yoy():
    return render_template('/blog_marathon_times_yoy.html')

@app.route('/blog_coronavirus_march',methods=['GET','POST'])
def blog_coronavirus_march():
    return render_template('/blog_coronavirus_march.html')

@app.route('/blog_coronavirus_april',methods=['GET','POST'])
def blog_coronavirus_april():
    return render_template('/blog_coronavirus_april.html')

@app.route('/blog_coronavirus_nj',methods=['GET','POST'])
def blog_coronavirus_nj():
    return render_template('/blog_coronavirus_nj.html')

@app.route('/blog_cptc_results',methods=['GET','POST'])
def blog_cptc_results():
    return render_template('/running/blog_cptc_results.html')

@app.route('/blog_amtrak_routes',methods=['GET','POST'])
def blog_amtrak_routes():
    return render_template('/blog_amtrak_routes.html')

@app.route('/amtrak_timeline_scroll',methods=['GET','POST'])
def amtrak_timeline_scroll():
    return render_template('/amtrak_timeline_scroll.html')

@app.route('/blog_southwest_2020',methods=['GET','POST'])
def blog_southwest_2020():
    return render_template('/blog_southwest_2020.html')

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

@app.route('/api/airline_2020_comp',methods=['GET','POST'])
def api_airlines_2020_comp():
    airport = request.form["airport"]
    print(airport)
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
    return send_df.to_json(orient='index')

@app.route('/api/airline_2020_comp_chart',methods=['GET','POST'])
def api_airlines_2020_comp_chart():
    airports = request.form["airports"].split(',')
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
    return jsonify({'airport_comp_script':airport_comp_script,'airport_comp_div':airport_comp_div})

@app.route('/airlines_in_2020',methods=['GET','POST'])
def airlines_in_2020():
    conn=sqlite3.connect('airport_comp_2020.db')
    airports=pd.read_sql("SELECT DISTINCT(A.AIRPORT),B.DISPLAY_AIRPORT_NAME FROM monthly_2020_2019_airport_comp as A "+
                 "LEFT JOIN airport_names as B ON A.AIRPORT=B.AIRPORT ORDER BY A.AIRPORT",conn)
    airport_list=airports.to_json(orient='split')
    if request.method =='GET':
        air_sel='STL'
    else:
        air_sel=request.form['airport']
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
    return render_template('/airlines_in_2020.html',air_sel=air_sel,totals_display=totals_display,pass_script=pass_script,pass_div=pass_div,
        dept_script=dept_script,dept_div=dept_div,seats_script=seats_script,seats_div=seats_div,
        airport_list=airport_list,routes_display=routes_display, latest_month_label= latest_month_label)

@app.route('/all_blogs',methods=['GET','POST'])
def all_blogs():
    return render_template('/all_blogs.html')

if __name__ == '__main__':
    app.run()
    #app.run(host='159.203.65.80',port=33506)


