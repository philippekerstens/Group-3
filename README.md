# Group-3
## Project Focus
### Our group topic is Hospital Bed Availability, something that we chose because of its importance in the face of this Covid Pandemic, especially in regards to the difficulty of the early weeks of the pandemic where medical supplies were lacking, and there were difficulties in finding beds in hospitals to deal with the surge in patients.
### It is this projects intention to compile a self-updating database of which it can be utilized by hospitals and governments on the local, state, and national level in keeping track of hospital bed availability as well as preventing overflow and being able to have oversight over vast regions to better handle emergencies like the pandemic.
### By creating this project database we will be able to not only track availability of hospitals during emergencies anv normal times, but also see which hospitals would need the most resources or assistance, especially with the county data which allows us to consider the per capita ratio of hospital bed availability.
## Why this project
### This project focus was chosen as we wished to choose something relevant to our current times and events, and in regards of covid, we discovered the potential for improving and avoiding these issues in the future, or at least aiding those that wish to avoid such crisises again.
## Links and Sources
### Slideshow  : https://docs.google.com/presentation/d/19MMd_3xDyaQTVIac4mx9ayKighQCOw1OY78eupEQc3c/edit?usp=sharing
### Database 1 : https://apidocs.covidactnow.org/ - API for covid data
### Database 2 : https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u - hospital aggregated data
### Database 3 : https://github.com/nytimes/covid-19-data - NYT data github page
### Database 4 : https://github.com/owid/covid-19-data - One World Data github page
### Database 5 : https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh - Vaccination data (CDC)

### Database Recreation instructions
1. Create a database called COVID_Risk_Final_Project in pgAdmin using the PostgreSQL 13 server.
2. Run the Deliverable_1_input_data.ipynb notebook in its entirety.
3. Using the query tool in pgAdmin on the COVID_Risk_Final_Project database, run the following queries to create primary keys for both tables: 
ALTER TABLE counties ADD PRIMARY KEY (fips_date); ALTER TABLE hospitals ADD PRIMARY KEY (fips_date);
4. Run the PLACEHOLDER TEXT notebook in its entirety to join the tables and connect the database to the machine learning model.

## Dashboard:
The layout of the dashboard can be viewed on our google slide presentation deck.  
### Technology for the dashboard:
The dashboard is being created using a flask app that is able to tap into our SQL database.  One we have acheived a connection to our database, we will be querying the data to use in our interactive map and charts on page 2 and 3 respectively.  We are using bootsrap and some custom CSS to sylyze the dashboard.  We are using D3 and javascript to work with and manipulate or data.

### Interactive elements:
On the main page we will have a description and overview of the project.  We will also have an interactive element on the page where the user can use a dropdown button to change between a top 10 list of either cases or deaths aggregated by county.  On the second page, the viewer will be able to enter in a fips code and the map will automatically load to a properly zoomed out veiw of the selected county.  Once the fips code is entered some recent covid-19 data about that county will also be presented.  On the third page, we will have the same fips code filter on the top of the page.  Once the fips code is entered the two charts below will populate with data specific to the filtered fips code.  Some ideas for the charts will be cases by date, deaths by date, or hospital bed capacity for that county.
