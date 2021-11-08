--Create counties table
CREATE TABLE counties (
	fips_date VARCHAR NOT NULL,
	fips FLOAT,
	dates DATE,
	cases FLOAT,
	deaths FLOAT,
	PRIMARY KEY (fips),
	UNIQUE (fips_date)
);

--Create hospitals table
CREATE TABLE hospitals (
	fips_date VARCHAR NOT NULL,
	collection_week DATE,
	fips_code FLOAT,
	total_beds_7_day_sum FLOAT,
	all_adult_hospital_beds_7_day_sum FLOAT,	
	all_adult_hospital_inpatient_beds_7_day_sum FLOAT,	
	inpatient_beds_used_7_day_sum FLOAT,	
	all_adult_hospital_inpatient_bed_occupied_7_day_sum FLOAT,	
	total_adult_patients_hospitalized_confirmed_and_suspected_covid_7_day_sum FLOAT,	
	total_adult_patients_hospitalized_confirmed_covid_7_day_sum FLOAT,	
	total_pediatric_patients_hospitalized_confirmed_and_suspected_covid_7_day_sum FLOAT,
	total_pediatric_patients_hospitalized_confirmed_covid_7_day_sum FLOAT,
	inpatient_beds_7_day_sum FLOAT,	
	total_icu_beds_7_day_sum FLOAT,	
	total_staffed_adult_icu_beds_7_day_sum FLOAT,	
	icu_beds_used_7_day_sum FLOAT,	
	staffed_adult_icu_bed_occupancy_7_day_sum FLOAT,	
	staffed_icu_adult_patients_confirmed_and_suspected_covid_7_day_sum FLOAT,	
	staffed_icu_adult_patients_confirmed_covid_7_day_sum FLOAT,
	FOREIGN KEY (fips_date) REFERENCES counties (fips_date),
	PRIMARY KEY (fips_date)
);

--Inner join the tables on fips_date
SELECT * FROM counties 
INNER JOIN hospitals
ON counties.fips_date = hospitals.fips_date