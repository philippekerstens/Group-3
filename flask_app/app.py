# To view the dashboard on the browser:
    # 1. Make sure all the dependencies or imported 
    # 2. Open the terminal and run python app.py
    # 3. Copy the web addres ('http://) and paste it into your browser
    # 4. Enjoy the dasboard

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
Counties = Base.classes.counties_charts
Hospitals = Base.classes.hospital_chart
Vaccinations = Base.classes.vaccinations_chart
#Vaccinations = Base.classes.vaccinations

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

@app.route('/api/case_data')
def case_data():
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

@app.route('/api/hospital_data')
def hospital_data():
    def hospital():
        if "fips_code" in session:
            fips_code = session['fips_code']
            capacity = se.query(Hospitals.collection_week, Hospitals.Percentage_inpatient_beds_used).\
                filter(Hospitals.fips_code == fips_code).all()

            capacity_by_date = {str(collection_week): Percentage_inpatient_beds_used for collection_week, Percentage_inpatient_beds_used in capacity}

            return(capacity_by_date)
    
    return jsonify(hospital())

@app.route('/api/vax_data')
def vax_data():
    def vax():
        if "fips_code" in session:
            fips_code = session['fips_code']
            vax = se.query(Vaccinations.Date, Vaccinations.Series_Complete_Pop_Pct).\
                filter(Vaccinations.FIPS == fips_code).all()

            vax_by_date = {str(Date): Series_Complete_Pop_Pct for Date, Series_Complete_Pop_Pct in vax}

            return(vax_by_date)
    
    return jsonify(vax())

if __name__ == '__main__':
    app.run()
