
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import create_engine, inspect
from flask import Flask, jsonify
from datetime import datetime





engine = create_engine("sqlite:///Resources/hawaii.sqlite")





# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# We can view all of the classes that automap found
Base.classes.keys()



# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station



# Create our session (link) from Python to the DB
session = Session(engine)

# query, loop over and print out measurements.
#hawaii_data = session.query(Measurement).filter(Measurement).all()
inspector = inspect(engine)
inspector.get_table_names()



columns = inspector.get_columns('measurement')
for c in columns:
    print(c['name'], c["type"])



engine.execute('SELECT * FROM measurement LIMIT 30').fetchall()



columns = inspector.get_columns('station')
for c in columns:
    print(c['name'], c["type"])



engine.execute('SELECT * FROM station LIMIT 30').fetchall()



# query to retrieve the last 12 months of precipitation 
# Calculate the date 1 year ago from the last data point in the database
session.query(Measurement.date).order_by(Measurement.date.desc()).first()



# prcp for last 12 months
last_date=datetime.date(2017, 8 ,23)
#last_12=last_date - dt.timedelta(dayes=12)
last_12_months=datetime.date(2016, 8 ,23)



prcp_last_12=session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > last_12_months).order_by(Measurement.date).all()



# Save the query results as a Pandas DataFrame and set the index to the date column
#data frame the ^ prcr_last_12
df = pd.DataFrame(prcp_last_12, columns=['date', 'prcp'])
df.head()



df=df.fillna(0)
df.head()



# Sort the dataframe by date
df=df.sort_values(by='date')
df.head()



# Use Pandas to calcualte the summary statistics for the precipitation data
df.describe()

# Design a query to show how many stations are available in this dataset?
session.query(Station.station).count()


# What are the most active stations? (i.e. what stations have the most rows)?
# List the stations and the counts in descending order.
active_stations = session.query(Measurement.station, func.count(Measurement.tobs).label('Observations'))                  .group_by(Measurement.station).order_by(func.count(Measurement.tobs)).all()    
active_stations



active_stations = pd.DataFrame(active_stations)



active_stations.sort_values(by='Observations', ascending = False)



# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature most active station?
temps = [
      func.min(Measurement.tobs),
      func.max(Measurement.tobs),
      func.avg(Measurement.tobs)]
temp_measures = session.query(*temps).all()
temp_measures



# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
top_station = session.query(Measurement.station, Measurement.tobs).filter(Measurement.station=="USC00519281").filter(Measurement.date > last_12_months).order_by(Measurement.date).all()
top_station=pd.DataFrame(top_station)
# load the results into a dataframe
observation_df = pd.DataFrame.from_records(top_station)
observation_df = observation_df.rename(columns={0: 'Station', 1: 'Date', 2:'Observations'})
print(observation_df.count())
observation_df.head()


# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

# function usage example
print(calc_temps('2012-02-28', '2012-03-05'))




# Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax 
# calculate the min/max/avg from last year that matches my trip date
trip_arrive = datetime.date(2017, 2, 1)
trip_leave = datetime.date(2017, 2, 15)
last_year = datetime.timedelta(days=365)
temp_avg_lst_year = (calc_temps((trip_arrive-last_year), (trip_leave-last_year)))
print(temp_avg_lst_year)




# Plot the results from your previous query as a bar chart. 
# Use "Trip Avg Temp" as your Title
# Use the average temperature for the y value
# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)

# plotting the data as a boxpl



# Calculate the total amount of rainfall per weather station for your trip dates using the previous year's matching dates.
# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation





from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the measurement and station tables
Measurement=Base.classes.measurement_table
Station=Base.classes.station_table

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################




# Complete the routes for your app here
# 3. Define what to do when a user hits the index route
@app.route("/")
def welcome():
   """List all available api routes."""
   return (
       f"Available Routes:<br/><br/>"
       f"/api/v1.0/precipitation - Precipitation<br/>"

       f"/api/v1.0/stations"
       f"- List of stations from the dataset<br/>"

       f"/api/v1.0/tobs"
       f"- Temperature Observations (tobs) for the previous year<br/>"

       f"/api/v1.0/&ltstart&gt"
       f"- Calculates MIN, AVG, and MAX temp. for all dates greater than and equal to the start date<br/>"

       f"/api/v1.0/&ltstart&gt/&ltend&gt"
       f"- Calculates MIN, AVG, and MAX temp. for a given start or start-end range<br/>"
   )





@app.route("/api/v1.0/precipitation")
def precipitation():
   prcp_last_12 = observation_df[["Date", "Observations"]]
   # prec_df = prec_df.set_index("Date")
   # return jsonify(prec_df.to_dict())
   return jsonify(prcp_last_12.to_dict())





@app.route("/api/v1.0/stations")
def stations():
   records = session.query(Station.station, Station.name).all()
   station_df = pd.DataFrame.from_records(records)
   station_df = station_df.rename(columns={0: 'Station', 1: 'Name'})
   return jsonify(station_df.to_dict())




@app.route("/api/v1.0/tobs")
def tobs():
   tobs_df = observation_df[["Date", "Observations"]]
   tobs_df = tobs_df.set_index("Date")
   return jsonify(tobs_df.to_dict())





def calc_temp_s(start_date):
   records = session.query(func.max(Measurement.tobs).label('max_temp'), func.avg(Measurement.tobs).label('avg_temp')                                ,func.min(Measurement.tobs).label('min_temp'))                  .filter(Measurement.date >= start_date).all()    
   return records[0]





@app.route("/api/v1.0/<start>")
def temp(start):
   max_tmp, avg_tmp, min_tmp = calc_temp_s(start)
   temp_dict = {"Max. Temp.": max_tmp,
                "Avg. Temp.": avg_tmp,
                "Min. Temp.": min_tmp}
   return jsonify(temp_dict)




@app.route("/api/v1.0/<start>/<end>")
def calc_temp_se(start, end):
   if datetime.strptime(start, '%Y-%m-%d') > datetime.strptime(end, '%Y-%m-%d'):
       records = calc_temps(start, end)
       max_tmp, avg_tmp, min_tmp = records[0]
       temp_dict = {"Max. Temp.": max_tmp,
                "Avg. Temp.": avg_tmp,
                "Min. Temp.": min_tmp}
       return jsonify(temp_dict)
   else:
       return "Please make sure Start Date is always greater than End Date."


   


# Create your app.run statement here
if __name__ == '__main__':
   app.run(debug=True)


