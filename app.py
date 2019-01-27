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
    conn=sqlite3.connect('t_100_segments.db')
    if request.method =='GET':
        carrier = "WN"
        airline_table=pd.read_sql(f'SELECT SUM(DEPARTURES_PERFORMED) AS DEPARTURES,SUM(SEATS) AS "TOTAL CAPACITY",SUM(PASSENGERS)\
            AS "TOTAL PASSENGERS", UNIQUE_CARRIER_NAME, DEST, DEST_CITY_NAME,YEAR FROM domestic_routes\
            WHERE ORIGIN="STL" AND UNIQUE_CARRIER="{carrier}" GROUP BY DEST,UNIQUE_CARRIER ORDER BY "TOTAL PASSENGERS" DESC', conn)
        airline_table=airline_table.loc[airline_table["TOTAL PASSENGERS"]>100]
        airline_table['LOAD FACTOR']=(airline_table['TOTAL PASSENGERS']/airline_table['TOTAL CAPACITY'])*100
        airline_table['LOAD FACTOR']=airline_table['LOAD FACTOR'].map('{:,.1f}%'.format)
        cols=airline_table.columns.tolist()
        airline_table=airline_table[cols[:3]+['LOAD FACTOR']+cols[3:-1]]
        air_dest = airline_table.values.tolist()
        print('h')
        return render_template('/all_airlines.html',airline_table=airline_table.to_html(classes='table table-striped my-table-all-air',index=False),air_dest=air_dest,var2='blank')
    else:
        dest_code = request.form['dest_code']
        print(dest_code)
        if dest_code!='':
            airline_table=pd.read_sql(f'SELECT SUM(DEPARTURES_PERFORMED) AS DEPARTURES,SUM(SEATS) AS "TOTAL CAPACITY",SUM(PASSENGERS)\
                AS "TOTAL PASSENGERS", UNIQUE_CARRIER_NAME, DEST, DEST_CITY_NAME,YEAR FROM domestic_routes\
                WHERE ORIGIN="STL" AND DEST="{dest_code}" GROUP BY DEST,UNIQUE_CARRIER ORDER BY "TOTAL PASSENGERS" DESC', conn)
        else:
            airline_table=pd.read_sql(f'SELECT SUM(DEPARTURES_PERFORMED) AS DEPARTURES,SUM(SEATS) AS "TOTAL CAPACITY",SUM(PASSENGERS)\
                AS "TOTAL PASSENGERS", UNIQUE_CARRIER_NAME, DEST, DEST_CITY_NAME,YEAR FROM domestic_routes\
                WHERE ORIGIN="STL" GROUP BY DEST,UNIQUE_CARRIER ORDER BY "TOTAL PASSENGERS" DESC', conn)
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
        
        air_dest = total_df.values.tolist()
        return render_template('/all_airlines.html',airline_table=total_df.to_html(classes='table table-striped my-table-all-air',index=False),air_dest=air_dest,var2=dest_code)        
    


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


