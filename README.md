# Group-3

## Purpose:
The purpose of this project is to help identify hospital systems that may need a reallocation of resources.  THe covid-19 pandemic has placed an incredible burden on the US healthcare system.  There is much evidence that many healthsystems are running low on hospital beds.  Through the covid 19 data we have analyzed, we hope to be able to predict whether a county's health system is at capacity or not.  This information could then be used to reassess the distribution of limited resources within the county.

## Goals:
* Show which county hospital systems are at limited bed capacity
* Show which county health systems are at high risk for overload
* Create an easy to use dashboard to visualize covid-19 data on a county by county basis
* Allow people to lookup their own local data
## Data:
Our data is being sourced from a multitude of sources.  Primarily the data is coming from the cdc, healthdata.gov, and the New York Times.  Links to several of the data sources can be seen below.
## Data Links:

1. https://apidocs.covidactnow.org/ - API for covid data
2. https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u - hospital aggregated data
3. https://github.com/nytimes/covid-19-data - NYT data github page
4. https://github.com/owid/covid-19-data - One World Data github page
5. https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh - Vaccination data (CDC)

## Things to do:
1. Host a S3 bucket to store the large data sets
2. Continue data cleaning process on current data sets
3. Merge data sets in Postgres
4. Import data from Postgres into ML model
5. Begin dashboard visualizations