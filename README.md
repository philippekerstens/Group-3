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
=======
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

##### Data Retrtieval
Data was exported from The New York Times (referred to as the 'counties' dataset), CDC ('vaccinations' dataset), and healthdata.gov ('hospitals' dataset). The three datasets were then loaded into S3 buckets as they are too large to upload to github.  

##### Intial Exploration and Database Creation
The initial data cleaning notebook, Deliverable_1_input_data, then uses pandas to read three datasets into individual dataframes. Unnecessary columns are then dropped from all three dataframes, including columns with categorical and some float data types, age range columns, and hospital coverage columns. The 'hospitals' dataset only contains weekly aggregations of its data, while the other two datasets contain daily reporting. The 'counties' and 'vaccinations' datasets are aggregated to report weekly totals on the same collection dates as 'hospitals'. To provide a common primary key among the three dataframes, the fips and date columns are turned into and string datatype and concatenated to fomr the fips_date coulmn. A list of unique fips_date values was generated and then removed from all three dataframes, to return equal length dataframes that can easily be merge in PostgreSQL. The remaining float data types are then converted to integers in all three dataframes. Column names are abbreviated to prevent truncating them in SQL. A connection string is then created using create_engine from sqlalchemy to create the schema and load the data into tables in PostgreSQL. After being loaded, the schema needs to be adjusted to create primary keys (fips_date) for the three tables. 

##### Secondary Data Cleaning
The data is then read back into the next notebook, Postgres to ML Model Connection, using a SQL join for 'counties' and 'hospitals' creating merged_df and using 'vaccinations' to create vaccinations_df. The two dataframes are then merged and redundant columns are dropped to create ml_ready_df, which contains data from all three tables. Percentage and totals columns are then created adding and/or dividing columns by one another. Infinite values are then changed to NaN and all null rows are dropped. Subsequently, four bar graphs that may fit into our interactive dashboard were generated for Multnomah County.

![Cases to Date Multnomah County](https://user-images.githubusercontent.com/86164867/143787419-8a8f823e-f181-4d8c-aa5c-fdd6ff51684a.png)
![Deaths to Date Multnomah County](https://user-images.githubusercontent.com/86164867/143787420-e7bc0afb-32da-4b38-9261-0f4f2d2bd875.png)
![Percent of Population Fully Vaccinated Multnomah County](https://user-images.githubusercontent.com/86164867/143787421-d5ec48ef-b9eb-4fab-a5bd-da8754701042.png)
![Percentage of Inpatient Beds Used Multnomah County](https://user-images.githubusercontent.com/86164867/143787423-037de28b-bf2b-49c9-a9b0-ccba9c70c00e.png)


### Database Recreation instructions
1. Create a database called COVID_Risk_Analysis in pgAdmin using the PostgreSQL 13 server.
2. Alter the config.py file to contain your Postgres password in the connection string.
3. Run the 'Deliverable_1_input_data.ipynb' notebook in its entirety.
4. Using the query tool in pgAdmin on the COVID_Risk_Analysis database, run the following queries to create primary keys for both tables: 
ALTER TABLE counties ADD PRIMARY KEY (fips_date); ALTER TABLE hospitals ADD PRIMARY KEY (fips_date); ALTER TABLE vaccinations ADD PRIMARY KEY (fips_date);
4. Run the 'ML_Model.ipynb' notebook in its entirety to join the tables and connect the database to the machine learning model.



=======
=======
## Part 2: Implementing the machine learning model -

### Machine Learning Model
1. Description of preliminary data preprocessing:

Both data sets were loaded into S3 buckets. String data type columns were removed from both data sets. The 'counties' data set was aggregated to show weekly totals instead of daily. All columns that reported an average from the 'hospitals' data set were removed, as the aggregation process would not return accurate results for ratios. Columns that reported 7 day coverage were dropped from the 'hospitals' data set. Age range columns were dropped from the 'hospitals' data set. The fips_date column was created for both tables which combined the collection date and the fips_code into string to give a primary key to each data set. The following word in columns of the 'hospitals' data set were abbreviated to prevent PostgreSQL from truncating the column names: confirmed, suspected, and pediatric. Negative values were converted to zero to eliminate large variances in the aggregated data. Rows in which the fips_date column did not have a match in the other data set were dropped from both data sets. Float data types were converted to integers for both data sets.

2. Preliminary feature of engineering:

The primary feature of this machine learning model is to classify facilities that are full (ICU bed capacity over 85%) or still spacious (ICU bed capacity lower than 85%). Since the data subset full is smaller than spacious, we oversample it to get meaningful conclusion. We used two method for oversampling, random oversample and SMOTE oversmaple. The goal is to get 80% accuracy with the classification. The other side of machine leaning model is to classify and build 3D model of vaccination completeness percentage, number of cases and percentage of ICU bed used using K-Mean clustering. 

3. How data was split into training and testing sets:

I used sample (n=3500) for the first model due to limitation on my personal device. In case of first model, data is splited with the random state of 42 so that it can generate same train and test sets for different models. It is also stratified with y to ensure train and test sets have same proportion of y data. In case of K-Mean, I sampled 7000 rows from vaccination completeness percentage, number of cases and percentage of ICU bed used due to device limitation. For clustering the data, number of cluster that I aim for is not defined thus the model will drop the number of centroid it find and run with random state of 5 to help it starts with same random data point as centroid. 

4. Model choice:

The dataset we have is manipulated for continous variables. Supervised machine learning models fits to the dataset we have and also incline to have somewhat pair variables. Thus it was difficult to presume which variables can have possible relationship each other outside of their pairs. Thus I used K-Means to observe the possible clusters among 3 different data columns from different dataset. I choosed 3-D model to visualize the relationship between them. I pulled out percentage of ICU bed capacity from one of our paired dataset, ICU bed used and ICU bed total, and classify it into binary format. In order to see the occupancy of ICU beds in facility, I used supervised machine learning model to classify because every dataset has it's fips code with. Through this we aim to determine which facility in which area are full with ICU.     

## Part 3: Creation of the dashboard -
## Dashboard:
The layout of the dashboard can be viewed on our google slide presentation deck.  

You can recreate the dashboard locally by first imorting the necessary imports and then running python app.py in the terminal.  Then copy the localhost web address in the terminal and paste it into a browser to veiw the dashboard.

### Technology for the dashboard:
The dashboard is being created using a flask app that is able to tap into our SQL database.  One we have acheived a connection to our database, we will be querying the data to use in our interactive map and charts on page 2 and 3 respectively.  We are using bootsrap and some custom CSS to sylyze the dashboard.  We are using D3 and javascript to work with and manipulate or data.

### Interactive elements:
On the main page we will have a description and overview of the project.  We will also have an interactive element on the page where the user can use a dropdown button to change between a top 10 list of either cases or deaths aggregated by county.  On the second page, the viewer will be able to enter in a fips code and the map will automatically load to a properly zoomed out veiw of the selected county.  Once the fips code is entered some recent covid-19 data about that county will also be presented.  On the third page, we will have the same fips code filter on the top of the page.  Once the fips code is entered the two charts below will populate with data specific to the filtered fips code.  Some ideas for the charts will be cases by date, deaths by date, or hospital bed capacity for that county.
=======
On the main page we will have a description and overview of the project.  There are two sections below the main project overview that detail both the data exploration and database creation, and the machine learning model process and analysis.  On the second page, the viewer will be able to enter in a fips code, which will then create a query of our database that is used to build multiple charts that are displayed on the following page.  The user can then enter a new fips code on the form page to reload the charts for that specific fips code.


### Please follow the links below to view our slide show presentation and view the raw data sources:
Slideshow  : https://docs.google.com/presentation/d/19MMd_3xDyaQTVIac4mx9ayKighQCOw1OY78eupEQc3c/edit?usp=sharing

Hospital data: https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u  

NYT data github page: https://github.com/nytimes/covid-19-data  

Vaccination data (CDC): https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh  


