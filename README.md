# Group-3

## Overview
The purpose of this project is to predict whether there will be enough bed for hospitals through machine learning. 
I sorted bed capacity binary (upper 80% - full, lower 80% - spacious). 
Since the minority group (full) is significantly smaller than spacious, I am going to oversample to predict. Random oversampling would manipulate the data because instances from the minority class are randomly selected and added to the minority class which means model adds number of hospital. Thus, I'll use SMOTE oversampling. It fits better because the occupied rate (usage count / total capacity) is continuous data. 
![스크린샷(124)](https://user-images.githubusercontent.com/85276431/140704380-fec326dd-122b-47c5-b9ac-a780bdaad6c7.png)
