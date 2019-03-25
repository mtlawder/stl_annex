from flask import Flask, render_template, redirect, request
from bokeh.plotting import figure, show, output_file
from bokeh.embed import autoload_server, components
from bokeh.models import Range1d
from bokeh.document import Document
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool, FixedTicker
import pandas as pd
import numpy as np
import sqlite3
import datetime
from datetime import datetime,timedelta
import re
import time



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

@app.route('/stl_pop',methods=['GET','POST'])
def stl_pop():
    conn=sqlite3.connect('stl_census.db')
    if request.method =='GET':
        return render_template('/stl_neighborhood_pop.html')
    else:
        neighborhood=request.form['neighborhood']
        nbh_table=pd.read_sql('SELECT * FROM neighborhood_pop WHERE neighborhood="%s"' %(neighborhood), conn)
        p1 = figure(title="Population Change")
        p1.line(pd.to_numeric(nbh_table['Year']), pd.to_numeric(nbh_table['Total Population'].str.replace(',','')))
        script, div = components(p1)
        return render_template('/stl_neighborhood_pop.html', nbh_table=nbh_table.to_html(classes='table table-striped',index=False), plot_script=script, plot_div=div)

@app.route('/all_airlines',methods=['GET','POST'])
def all_airlines():
    conn=sqlite3.connect('t_100_segments_forgit.db')
    if request.method =='GET':
        carrier = "WN"
        airline_table=pd.read_sql(f'SELECT SUM(DEPARTURES_PERFORMED) AS DEPARTURES,SUM(SEATS) AS "TOTAL CAPACITY",SUM(PASSENGERS)\
            AS "TOTAL PASSENGERS", UNIQUE_CARRIER_NAME, DEST, DEST_CITY_NAME,YEAR FROM domestic_routes\
            WHERE ORIGIN="STL" AND YEAR=2017 AND UNIQUE_CARRIER="{carrier}" GROUP BY DEST,UNIQUE_CARRIER ORDER BY "TOTAL PASSENGERS" DESC', conn)
        airline_table=airline_table.loc[airline_table["TOTAL PASSENGERS"]>100]
        airline_table['LOAD FACTOR']=(airline_table['TOTAL PASSENGERS']/airline_table['TOTAL CAPACITY'])*100
        airline_table['LOAD FACTOR']=airline_table['LOAD FACTOR'].map('{:,.1f}%'.format)
        cols=airline_table.columns.tolist()
        airline_table=airline_table[cols[:3]+['LOAD FACTOR']+cols[3:-1]]
        air_dest = airline_table.values.tolist()
        carriers = list(set(airline_table["UNIQUE_CARRIER_NAME"].tolist()))
        print(carriers)
        return render_template('/all_airlines.html',airline_table=airline_table.to_html(classes='table table-striped my-table-all-air', \
            index=False),air_dest=air_dest,var2='ALL',airport_sel='STL',carriers=carriers,regional_sel='mainline',month_sel=0, \
            year_sel=2017,depart_arrive='depart',plot_air="",plot_air_script="")
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
        #combined_org_insert=""
        cols_insert="A.DEST, DEST_CITY_NAME"
        groupby_insert="A.DEST"
        origin_insert=f'A.ORIGIN="{airport_sel}"'
        year_insert="AND A.YEAR=2017"
        if month_sel!='0':
            month_insert="AND A.MONTH="+str(month_sel)
        if carrier_sel!='ALL' and carrier_sel!='ALL_SELECTED':
            carrier_insert='AND A.UNIQUE_CARRIER_NAME="'+str(carrier_sel)+'"'
        if depart_arrive == 'depart':
            if dest_code!='' and dest_code!='ALL':
                dest_insert='AND A.DEST="'+str(dest_code)+'"'
        elif depart_arrive == 'arrive':
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
        if regional_sel=='mainline':
            airline_table=pd.read_sql(f'SELECT SUM(DEPARTURES) AS DEPARTURES,SUM("TOTAL CAPACITY") AS "TOTAL CAPACITY",SUM("TOTAL PASSENGERS") \
                AS "TOTAL PASSENGERS", UNIQUE_CARRIER_NAME, DEST, DEST_CITY_NAME,YEAR FROM \
                (SELECT SUM(DEPARTURES_PERFORMED) AS DEPARTURES,SUM(SEATS) AS "TOTAL CAPACITY",SUM(PASSENGERS) \
                AS "TOTAL PASSENGERS", COALESCE(mainline_desc,UNIQUE_CARRIER_NAME) AS UNIQUE_CARRIER_NAME, \
                {cols_insert},A.YEAR FROM domestic_routes AS A LEFT JOIN regional_conversion as B \
                ON A.ORIGIN=B.origin AND A.DEST=B.destination AND A.UNIQUE_CARRIER=B.regional_code WHERE \
                ({origin_insert} {year_insert} {dest_insert} {carrier_insert} {month_insert}) {combined_insert} GROUP BY {groupby_insert}, \
                UNIQUE_CARRIER_NAME) AS COMB GROUP BY DEST,UNIQUE_CARRIER_NAME ORDER BY "TOTAL PASSENGERS" DESC', conn)
        else:
            airline_table=pd.read_sql(f'SELECT SUM(DEPARTURES_PERFORMED) AS DEPARTURES,SUM(SEATS) AS "TOTAL CAPACITY",SUM(PASSENGERS) \
                AS "TOTAL PASSENGERS", UNIQUE_CARRIER_NAME, \
                {cols_insert},A.YEAR FROM domestic_routes AS A LEFT JOIN regional_conversion as B \
                ON A.ORIGIN=B.origin AND A.DEST=B.destination AND A.UNIQUE_CARRIER=B.regional_code WHERE \
                ({origin_insert} {year_insert} {dest_insert} {carrier_insert} {month_insert}) {combined_insert} GROUP BY {groupby_insert},UNIQUE_CARRIER_NAME ORDER BY "TOTAL PASSENGERS" DESC', conn)

        airline_table=airline_table.loc[airline_table["TOTAL PASSENGERS"]>100]
        airline_table['LOAD FACTOR']=(airline_table['TOTAL PASSENGERS']/airline_table['TOTAL CAPACITY'])*100
        airline_table['LOAD FACTOR']=airline_table['LOAD FACTOR'].map('{:,.1f}%'.format)

        total_df=pd.DataFrame(columns=['DEPARTURES','TOTAL CAPACITY','TOTAL PASSENGERS','LOAD FACTOR',\
        'UNIQUE_CARRIER_NAME','DEST','DEST_CITY_NAME','YEAR'\
        ],data=[[airline_table["DEPARTURES"].sum(),airline_table["TOTAL CAPACITY"].sum(),airline_table["TOTAL PASSENGERS"].sum(),\
        (airline_table["TOTAL PASSENGERS"].sum()/airline_table["TOTAL CAPACITY"].sum())*100,"ALL SELECTED","ALL","ALL","ALL"]])
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
           title="Passenger Counts", toolbar_location=None, tools="")
            p1.vbar(x=list(p_air_tab['YEAR'].astype(str)+'-'+p_air_tab['MONTH'].astype(str)), top=list(p_air_tab['PASS']/1000), width=0.9)
            p1.xgrid.grid_line_color = None
            p1.y_range.start = 0
            p1.xaxis.major_label_orientation = 1.2
            p1.yaxis.axis_label= "Thousands of Passengers"
            script, div = components(p1)
        return render_template('/all_airlines.html',airline_table=total_df.to_html(classes='table table-striped my-table-all-air',index=False)\
            ,air_dest=air_dest,var2=dest_code,airport_sel=airport_sel,carriers=carriers,regional_sel=regional_sel,month_sel=month_sel,\
            year_sel=year_sel,depart_arrive=depart_arrive,plot_air=div,plot_air_script=script)        
    


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

if __name__ == '__main__':
    app.run()
    #app.run(host='159.203.65.80',port=33506)


