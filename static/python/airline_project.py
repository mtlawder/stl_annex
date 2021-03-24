import pandas as pd
import sqlite3
from bokeh.plotting import figure, ColumnDataSource
from bokeh.embed import components
from bokeh.models import HoverTool

def airline_project_get(conn):
    d_ops=pd.read_sql('SELECT ORIGIN, DEST, PASSENGERS FROM domestic_routes\
        WHERE (ORIGIN IN ("STL","IND","DSM","MCI","MEM","CVG","SBN","COU","SGF")) AND PASSENGERS>100 GROUP BY ORIGIN, DEST', conn)
    dest_options={city: list(d_ops[d_ops["ORIGIN"]==city]["DEST"]) for city in ["STL","IND","DSM","MCI","MEM","CVG","SBN","COU","SGF"]}
    carrier = "WN"
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
    return airline_table, air_dest, carriers, dest_options

def airline_project_post(dest_code,airport_sel,carrier_sel,regional_sel,month_sel,year_sel,depart_arrive,conn):
    month_insert =""
    carrier_insert =""
    dest_insert=""
    combined_insert = ""
    join_insert=""
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
    if year_sel=='All':
        year_insert=""
    else:
        year_insert='AND A.YEAR="'+str(year_sel)+'"'
        print(origin_insert,year_insert,dest_insert,carrier_insert,month_insert,combined_insert,groupby_insert,cols_insert)
    d_ops=pd.read_sql('SELECT ORIGIN, DEST, PASSENGERS FROM domestic_routes\
        WHERE (ORIGIN IN ("STL","IND","DSM","MCI","MEM","CVG","SBN","COU","SGF")) AND PASSENGERS>100 GROUP BY ORIGIN, DEST', conn)
    dest_options={city: list(d_ops[d_ops["ORIGIN"]==city]["DEST"]) for city in ["STL","IND","DSM","MCI","MEM","CVG","SBN","COU","SGF"]}
    if regional_sel=='mainline':
        airline_table=pd.read_sql(f'SELECT SUM(DEPT_ADJ) AS DEPARTURES,SUM(SEATS_ADJ) AS "TOTAL CAPACITY",SUM(PASS_ADJ) AS "TOTAL PASSENGERS",B.UNIQUE_CARRIER_NAME,\
            DEST,DEST_CITY_NAME,YEAR,ORIGIN,ORIGIN_CITY_NAME FROM domestic_routes AS A LEFT JOIN carrier_mapping AS B ON A.MAIN_CARRIER=B.UNIQUE_CARRIER \
            WHERE ({origin_insert} {year_insert} {dest_insert} {carrier_insert} {month_insert}) {combined_insert} \
            GROUP BY {groupby_insert},MAIN_CARRIER ORDER BY "TOTAL PASSENGERS" DESC', conn)
    else:
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
    air_dest = total_df.values.tolist()
    script=""
    div=""
    if dest_code!='' and dest_code!='ALL':
        p_air_tab=pd.read_sql(f'SELECT SUM(PASSENGERS) AS PASS, YEAR, MONTH FROM domestic_routes AS A WHERE {origin_insert} \
        {dest_insert} {carrier_insert} GROUP BY YEAR, MONTH', conn)
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
    return total_df,air_dest,carriers,div,script,dest_options