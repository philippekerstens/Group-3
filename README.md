# Group-3

## Overview
The purpose of this project is to predict whether there will be enough bed for hospitals through machine learning and to determine number of beds in need through the linear regression analysis. 
I sorted bed capacity binary (upper 85% - full, lower 85% - spacious). 
Since the minority group (full) is significantly smaller than spacious, I am going to oversample with various method (random oversample, SMOTE oversample and SMOTEEN sample) to predict. 

## Random Oversampling 
![스크린샷(125)](https://user-images.githubusercontent.com/85276431/141723097-278c9288-35f0-4116-9f72-f3e18964dbbe.png)
Accuracy score = 0.6213053613053613
## SMOTE oversample
![스크린샷(126)](https://user-images.githubusercontent.com/85276431/141723124-afa5fe46-5e30-4c2c-861b-7d9f039a3d42.png)
Accuracy score = 0.6161771561771562
## SMOTEEN sample
![스크린샷(128)](https://user-images.githubusercontent.com/85276431/141723230-5760e306-bed6-4be8-9262-79110cb5050e.png)
Accuracy score = 0.6156643356643356
## Linear regression 
