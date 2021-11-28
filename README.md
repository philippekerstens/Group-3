# Group-3
## Project Focus:
Our group topic is Hospital Bed Availability, something that we chose because of its importance in the face of the Covid-19 Pandemic, especially in regards to the difficulty of the early weeks of the pandemic where medical supplies were lacking, and there were difficulties in finding beds in hospitals to deal with the surge in patients.  It is this projects intention to compile a database that can be utilized by healthcare and county officials to recognize when their healthcare systems begin to become overloaded.

## Why this project:
This project focus was chosen as we wished to choose something relevant to our current times and events.  We feel strongly that the proper allocation of resources is paramount to getting us all through this pandemic.

## How this project is set up:
This project was created in 3 main parts.
  * Phase 1: Data retrival, exploration, and database creation
  * Phase 2: Implementing the machine learning model
  * Phase 3: Creation of the dashboard

## Part 1: Data retrival, exploration, and database creation - 

### Database Recreation instructions
1. Create a database called COVID_Risk_Final_Project in pgAdmin using the PostgreSQL 13 server.
2. Alter the config.py file to contain your Postgres password.
3. Run the Deliverable_1_input_data.ipynb notebook in its entirety.
4. Using the query tool in pgAdmin on the COVID_Risk_Final_Project database, run the following queries to create primary keys for both tables: 
ALTER TABLE counties ADD PRIMARY KEY (fips_date); ALTER TABLE hospitals ADD PRIMARY KEY (fips_date);
4. Run the 'Postgres to ML Model' notebook in its entirety to join the tables and connect the database to the machine learning model.


## Part 2: Implementing the machine learning model -

### Machine Learning Model
1. Description of preliminary data preprocessing:

Both data sets were loaded into S3 buckets. String data type columns were removed from both data sets. The 'counties' data set was aggregated to show weekly totals instead of daily. All columns that reported an average from the 'hospitals' data set were removed, as the aggregation process would not return accurate results for ratios. Columns that reported 7 day coverage were dropped from the 'hospitals' data set. Age range columns were dropped from the 'hospitals' data set. The fips_date column was created for both tables which combined the collection date and the fips_code into string to give a primary key to each data set. The following word in columns of the 'hospitals' data set were abbreviated to prevent PostgreSQL from truncating the column names: confirmed, suspected, and pediatric. Negative values were converted to zero to eliminate large variances in the aggregated data. Rows in which the fips_date column did not have a match in the other data set were dropped from both data sets. Float data types were converted to integers for both data sets.

2. Preliminary feature of engineering:

Linear regression 1 model is designed to predict number of beds needs for COVID patient for facilities. Since our data is collected in weekly base, users can input past weeks data (number of patients who are or might have COVID-19)  into the model to predict the number of beds that will be used for upcoming week. Linear regression model 2 model is designed to predict the number of deaths through the number of cases. The number of cases and deaths per week are selected for linear regression model and it will estimate the relationship between independent variable(cases) and one dependent variable(deaths). Additionally, for linear regression model 2, another variable (adult patients who are in ICU bed for COVID) is added to give further estimation of correlation of death and thr rest two variables. 

3. How data was split into training and testing sets:

For both linear regression model, dependent variable X is reshaped to specify the number of rows and columns. They are fitted (trained) to see the patterns in the data and generate prediction of independent variable(bed needed and deaths). The additional variable (adult patients who are in ICU bed for COVID) and cases for linear regression model 2 is splited into training and testing 0.8 : 0.2. We want to keep 20% of the data subset of the entire dataset for the testing purposes and training the rest 80% for prediction. X train and y train subsets are trained and output is predicted by following tested dependent variables. The accuracy performance of the model 2 was 0.903 which we can be concluded it's prediction is accurate up to 90% of the time. 

4. Model choice:

The dataset we have is manipulated for continous variables. Supervised machine learning models fits to the dataset we have and also incline to have somewhat pair variables. Thus it was difficult to presume which variables can have possible relationship each other outside of their pairs. Linear regression model can be most effective tool to analyze these paird associated variables. The limitation of our model it's linearity. Due to multiple possible causes that are not counted in our dataset, it's linearity could be temporary (vaccination status, weather and location) or irrelevant because strong correlation does not mean it is cause and effect relationship. The benefit of linear regression is that we can build and see the relationship between the variables intuitively that could have cause and effect relationship. It is easier to interpret compare to other side of machine learning methods, which can provide meaningful relationships with what dataset we have.   

## Part 3: Creation of the dashboard -

## Dashboard:
The layout of the dashboard can be viewed on our google slide presentation deck.  
### Technology for the dashboard:
The dashboard is being created using a flask app that is able to tap into our SQL database.  One we have acheived a connection to our database, we will be querying the data to use in our interactive map and charts on page 2 and 3 respectively.  We are using bootsrap and some custom CSS to sylyze the dashboard.  We are using D3 and javascript to work with and manipulate or data.

### Interactive elements:
On the main page we will have a description and overview of the project.  We will also have an interactive element on the page where the user can use a dropdown button to change between a top 10 list of either cases or deaths aggregated by county.  On the second page, the viewer will be able to enter in a fips code and the map will automatically load to a properly zoomed out veiw of the selected county.  Once the fips code is entered some recent covid-19 data about that county will also be presented.  On the third page, we will have the same fips code filter on the top of the page.  Once the fips code is entered the two charts below will populate with data specific to the filtered fips code.  Some ideas for the charts will be cases by date, deaths by date, or hospital bed capacity for that county.


### Please follow the links below to view our slide show presentation and view the raw data sources:
Slideshow  : https://docs.google.com/presentation/d/19MMd_3xDyaQTVIac4mx9ayKighQCOw1OY78eupEQc3c/edit?usp=sharing

Hospital data: https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u  

NYT data github page: https://github.com/nytimes/covid-19-data  

Vaccination data (CDC): https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh  

