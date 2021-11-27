import datetime as dt

from flask.helpers import url_for
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session as Se
from sqlalchemy import create_engine, func
from config import connection_string

from flask import Flask, jsonify, render_template, request, redirect, session

# Create engine using the database file
engine = create_engine(connection_string)
Base = automap_base()
Base.prepare(engine, reflect=True)
dbConnection = engine.connect()
# Create references to the database
Counties = Base.classes.counties
Hospitals = Base.classes.hospitals

# Create a session
se = Se(engine)


app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['POST', 'GET'])
def form():
    if request.method == 'POST':
        fips_code = request.form['fc']
        session['fips_code'] = fips_code
        return redirect(url_for("charts"))
    else:
        return render_template('form.html')


@app.route('/charts')
def charts():
    if "fips_code" in session:
        fips_code = session['fips_code']
        return render_template("page3.html")
    else:
        return redirect(url_for('form'))
    # if request.method == 'GET':
    #     return render_template('page3.html')
    # if request.method == 'POST':
    #     fips_code = request.form['fc']
    #     return render_template('page3.html', fips_code=fips_code)
        #redirect(url_for('death_data', fips_code = death_data))
   # return render_template('page3.html')

@app.route('/api/case_data')
def case_data():
    cases = se.query(Counties.collection_week, Counties.cases_to_date).\
        filter(Counties.collection_week >= '2021-01-01').all()
    
    precip = {str(collection_week): cases_to_date for collection_week, cases_to_date in cases}


    # This code selects the desired county and queries the database to pull up only dates and cases for that county
    def cases():
        if "fips_code" in session:
            fips_code = session['fips_code']
            county = se.query(Counties.collection_week, Counties.cases_to_date).\
                filter(Counties.fips == fips_code).all() # need to get the filter to be the javascript variable

            county_by_date = {str(collection_week): cases_to_date for collection_week, cases_to_date in county}

            # c = session.query(Counties.collection_week, Counties.fips, Counties.cases_to_date).all()
            # c_json = {fips: collection_week, cases_to_date for fips, collection_week, cases_to_date in c}
            
            return(county_by_date)

    return jsonify(cases())

@app.route('/api/death_data')
def death_data():
    def deaths():
        if "fips_code" in session:
            fips_code = session['fips_code']
            deaths = se.query(Counties.collection_week, Counties.deaths_to_date).\
                filter(Counties.fips == fips_code).all()

            deaths_by_date = {str(collection_week): deaths_to_date for collection_week, deaths_to_date in deaths}

            return(deaths_by_date)
    
    return jsonify(deaths())

if __name__ == '__main__':
    app.run()
