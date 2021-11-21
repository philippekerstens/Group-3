# Group-3
### Database Recreation instructions
1. Create a database called COVID_Risk_Final_Project in pgAdmin using the PostgreSQL 13 server.
2. Run the Deliverable_1_input_data.ipynb notebook in its entirety.
3. Using the query tool in pgAdmin on the COVID_Risk_Final_Project database, run the following queries to create primary keys for both tables: 
ALTER TABLE counties ADD PRIMARY KEY (fips_date); ALTER TABLE hospitals ADD PRIMARY KEY (fips_date);
4. Run the PLACEHOLDER TEXT notebook in its entirety to join the tables and connect the database to the machine learning model.
