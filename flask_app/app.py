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

    cases = session.query(Counties.collection_week, Counties.cases_to_date).\
        filter(Counties.collection_week >= '2021-01-01').all()
    
    precip = {str(collection_week): cases_to_date for collection_week, cases_to_date in cases}

    return jsonify(precip)


if __name__ == '__main__':
    app.run()
