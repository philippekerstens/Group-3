# Wednesday 11/10 class instructions
Hey guys, I will not be able to attend class tonight. Below are instructions for how to acquire and preliminarily clean the data.  

1. Download full data set (I will refer to it as the hospitals data) from the following link: https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u Use the export button in the upper right hand corner to get the full dataset, the API will only give you the first 1000 rows.
2. Download the full data set (I will refer to it as the counties data) from the following link: https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv There is a trick to downloading this data that I cannot remember, but David should be able to talk us through how to download it. 
3. Once the input data is stored locally, run all cells in the Deliverable_1_input_data.ipynb notebook found in this branch. This will export cleaned and prepared data to enter in the SQL database and directly into the machine learning model. I am not able to post the cleaned sets as they are too large to host on Git Hub.  I will finish setting up the SQL database this weekend, but we should not need it for our purposes this week. 

Missing data transformation:
1. We are currently missing is a way to find the weekly aggregation for the counties data, instead of the total aggregation. We can also discuss eliminating this step if we prefer.
2. In order to aggregate the hospital data set I had to eliminate all columns that proveded averages. We need to remake these columns by creating calculations for the sum columns.





# Group-3

The 'Deliverable_1_input_data' notebook takes in CSV files from healthdata.gov and the NEw York Times. It then eliminates unnecessary columns, changes the data type of the date column, and aggregates data based on reporting week and fips code. We then added another column to both CSVs, fips_date, so that both would have a unique identifier.

### Database Recreation Instructions
The database can recreated by running the schema.sql in it's entirety, in the order it is written. We are, however, still experiencing issues with loading our data. We have repeatedly encountered the following error: 'ERROR:  invalid input syntax for type double precision: "7/31/2020"CONTEXT:  COPY counties, line 2, column fips: "7/31/2020".
