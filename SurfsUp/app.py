# Import the dependencies.

import datetime as dt
from datetime import timedelta, date
import warnings

from flask import Flask, jsonify

from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


warnings.filterwarnings('ignore')

#################################################
# Helper Functions
#################################################

def query_to_json(query):
    """ Converts a query object into a Json object """
    dict_list = []
    # Converting every row of the class in query in to a dictionary
    for instance in query:
        dict = {}
        # Get values in every instance
        for key, value in instance.__dict__.items():
            # Skip the hidden properties
            if key[0] != '_':
                dict[key] = value
        dict_list.append(dict)
    return jsonify(dict_list)

def convert_to_date_time(date_string):
    """ Change the type of the input date to Datetime """
    d = dt.datetime.strptime(date_string, "%Y-%m-%d")
    return d
            
#################################################
# Database Setup
#################################################

engine = create_engine('sqlite:///./Resources/hawaii.sqlite')
Base = automap_base()
# reflect an existing database into a new model
Base.prepare(autoload_with=engine)
# reflect the tables
Base.classes.keys()
# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Home Page
@app.route("/")
def Welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>" 
        f"/api/v1.0/enter_start_date<br/>"
        f"/api/v1.0/enter_start_date/enter_end_date"
     )

# Precipitation page
@app.route("/api/v1.0/precipitation")
def precipitation():
    """last 12 months of precipitation data."""
    session = Session(bind=engine)
    # Find most resent data
    recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    # Calculate the date one year from the last date in data set.
    one_year_before = convert_to_date_time(recent_date[0]) - dt.timedelta(days=365)
     # Perform a query to retrieve the data and precipitation scores
    results = session.query(measurement.date, measurement.prcp).\
        filter(
            measurement.date >= one_year_before
    ).order_by(
            measurement.date.desc()
    ).all()
    session.close()
    # Creat dictionary from the row data and append to a precepitation list. 
    precepitation = []
    for date, prcp in results:
       prcp_dict = {}
       prcp_dict[date] = prcp
       precepitation.append(prcp_dict) 
    return jsonify(precepitation)

# Stations page
@app.route("/api/v1.0/station")
def stations():
    """ List of all stations"""
    session = Session(bind=engine)
    # Run query to get all stations.
    results = session.query(station).all()
    session.close()
    return query_to_json(results)

# Tobs page
@app.route("/api/v1.0/tobs")
def tobs():
    """   
    The dates and temperature observations of the most-active station 
    for the previous year of data. 
    """
    session = Session(bind=engine)
    # Finding most active station
    most_active = session.query(
        measurement.station,
        func.count(measurement.station)
    ).group_by(measurement.station).\
    order_by(
        func.count(measurement.station).desc()
    ).first()[0]
    # Find most resent data
    recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    # Calculate the date one year from the last date in data set.
    one_year_before = convert_to_date_time(recent_date[0]) - dt.timedelta(days=365)
    # Qury the date and temps of most active station for the past year
    results = session.query(measurement.date, measurement.tobs).\
        filter(
            measurement.date >= one_year_before,
            measurement.station == most_active
    ).order_by(
        measurement.date.desc()
    ).all()
    session.close()

    tempreture = []
    for date, tobs in results:
       tobs_dict = {}
       tobs_dict[date] = tobs
       tempreture.append(tobs_dict)
    return jsonify(tempreture)

# Tempreture summary after a date
@app.route("/api/v1.0/<start>")
def s_date(start):
    """ Min, Max and average of the tempreture """
    d = convert_to_date_time(start)
    session = Session(bind=engine)
    # Query the Data
    results = session.query(
        func.min(measurement.tobs),
        func.max(measurement.tobs),
        func.avg(measurement.tobs)
    ).filter(
        measurement.date >=  d
    ).first()
    session.close()
    tempreture = []
    temp_dict = {}
    min_t, max_t, avg_t = results
    temp_dict["min"] = min_t
    temp_dict["max"] = max_t
    temp_dict["avg"] = avg_t
    tempreture.append(temp_dict)
    return jsonify(tempreture)

# Tempreture summary between two dates
@app.route("/api/v1.0/<start>/<end>")
def s_e_date(start, end):
    """ Min, Max and average of the tempreture """
    s = convert_to_date_time(start)
    e = convert_to_date_time(end)
    session = Session(bind=engine)
    # Query the Data
    results = session.query(
        func.min(measurement.tobs),
        func.max(measurement.tobs),
        func.avg(measurement.tobs)
    ).filter(
        measurement.date >=  s,
        measurement.date <=  e 
    ).first()
    session.close()
    tempreture = []
    temp_dict = {}
    min_t, max_t, avg_t = results
    temp_dict["min"] = min_t
    temp_dict["max"] = max_t
    temp_dict["avg"] = avg_t
    tempreture.append(temp_dict)
    return jsonify(tempreture)


if __name__ == '__main__':
    app.run(debug=True)
