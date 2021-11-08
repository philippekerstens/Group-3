# Group-3

The 'Deliverable_1_input_data' notebook takes in CSV files from healthdata.gov and the NEw York Times. It then eliminates unnecessary columns, changes the data type of the date column, and aggregates data based on reporting week and fips code. We then added another column to both CSVs, fips_date, so that both would have a unique identifier.

### Database Recreation Instructions
The database can recreated by running the schema.sql in it's entirety, in the order it is written. We are, however, still experiencing issues with loading our data. We have repeatedly encountered the following error: 'ERROR:  invalid input syntax for type double precision: "7/31/2020"CONTEXT:  COPY counties, line 2, column fips: "7/31/2020".
