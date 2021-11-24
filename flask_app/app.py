import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from config import connection_string

from flask import Flask, jsonify, render_template

# Create engine using the database file
engine = create_engine(connection_string)
Base = automap_base()
Base.prepare(engine, reflect=True)
dbConnection = engine.connect()
# Create references to the database
Counties = Base.classes.counties
Hospitals = Base.classes.hospitals

# Create a session
session = Session(engine)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/maps')
def maps():
    return render_template('page2.html')

@app.route('/charts')
def charts():
    return render_template('page3.html')

@app.route('/api/chart_data')
def chart_data():

    cases = session.query(Counties.collection_week, Counties.cases_to_date).\
        filter(Counties.collection_week >= '2021-01-01').all()
    
    precip = {str(collection_week): cases_to_date for collection_week, cases_to_date in cases}


    # This code selects the desired county and queries the database to pull up only dates and cases for that county
    def cases():

        county = session.query(Counties.fips_date, Counties.cases_to_date).all()
            #filter(Counties.fips == '1001.0').all() # need to get the filter to be the javascript variable

        county_by_date = {str(fips_date): cases_to_date for fips_date, cases_to_date in county}

        # c = session.query(Counties.collection_week, Counties.fips, Counties.cases_to_date).all()
        # c_json = {fips: collection_week, cases_to_date for fips, collection_week, cases_to_date in c}
        
        return(county_by_date)

    return jsonify(cases())


if __name__ == '__main__':
    app.run()
