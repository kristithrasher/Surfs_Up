# Build Flask routes    
# import dependencies
import datetime as dt
import numpy as np
import pandas as pd
# Add the SQLAlchemy dependencies 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import the dependencies that we need for Flask.
from flask import Flask, jsonify

# Set up the database engine this create_engine function allows us to 
# acess and query our database
engine = create_engine("sqlite:///hawaii.sqlite")


#reflect the database into our classes
Base = automap_base()

# reflect the database
Base.prepare(engine, reflect=True)

# create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)

# Set up Flask
app = Flask(__name__)


# Create the welcome route
@app.route("/")


# create a function welcome() with a return statement
def welcome():
    # add the precipitation, stations, tobs, and temp routes that we'll need for this module into 
    # our return statement. We'll use f-strings to display them for our investors:
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#create the route for precipitation
@app.route("/api/v1.0/precipitation")

# Create the second route  precipitation function add calculation from a year ago from date specified 
# get the data for precipitation for following year
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   
   # write a query to get the date and precipitation for the previous year.
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   
    # create a dictionary with the date as the key and the precipitation /n
    #  as the value. jsonify the dictionary. Use Jsonify() function that converts /n         # the dictionary to a JSON file.
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


# create the route for stations
@app.route("/api/v1.0/stations")

# Create a function for stations
def stations():
    # create a query to get all the stations in our database
    results = session.query(Station.station).all()
    # Place results into a one-dimensional array (to do this use function np.ravel())
    stations = list(np.ravel(results))
    # note must set stations = stations to return a list
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")

# create a function temp_monthly to return the temperature observations for the previous year
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# create statistics route called stats
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create a function  to see the minimum, maximum, and average temperatures
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)