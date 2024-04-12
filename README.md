# Predictive Crime Analysis First Prototype Using Streamlit
* Author: Leena Goyal [@Leena2403](https://www.github.com/Leena2403) and Souryadeepta Majumdar [@majumdarsouryadeepta](https://www.github.com/majumdarsouryadeepta)
* Created on: April 12, 2024
* Description: Data analysis, exploration & visualization on crime incidents in Karnataka
* Curated dataset: Provided by KSP


#### Main Interface Look 
![](Visualisations/interface%20look.png?raw=true)
  

# Solutions Provided

- Spatial analysis of the crime, distribution of crimes over a particular location, and crime hotspots.

- Location-based analysis of the crimes, beat-wise distribution of crimes.

- Trend of occurrence of crimes at a particular time or in a particular day/month/season of the year.

- Analysis of the accused age, occupation, socio-economic status, location, etc., and prediction of criminal behavior.

- Analysis of the victim, socio-economic background, gender, location, and prediction of vulnerable populations and areas.

- Comparison of beat duties, patrolling areas with that of the crime occurrence, and analyzing the performance of the police.


# Crime Datasets

The datasets provided and used include 

- **FIR Dataset**
    - 2016 - 2024
- **Accused Dataset**
    - 2016 - 2024
- **Victim Dataset**
    - 2016 - 2024
- **Arrest Dataset**
    - 2016 - 2024
  

The data ranges from 01/2016 to 02/2024. The goal is to try to predict the category of crime that occurred in the various districts of Karnataka. Alongside, comprehensive accused analysis and victim analysis is made. Dynamic and interactive spatial and location based analysis is present.

Using Scikit Learn, predictions have been made for both crime and criminal analysis. Proper Victim Analysis has also been done.

## Files

## Folders
**Visualisationss**
- [Analysis]([https://github.com/Leena2403/main](https://github.com/Leena2403/predictive-crime-analysis-first_prototype/edit/main/Visualizations) - The main visualisations from our web app providing the png files for bar graphs, line plots and maps.
- Districtwise plotting of crime along with the heat maps is present.
- Vulnerable crime areas are included using records of victim analysis. Folium is being used to display the auto-generated html files.

**Data Predictions**

- [Crime Prediction]([https://github.com/k-chuang/kaggle-sf-crime/blob/master/cv_results](https://github.com/Leena2403/predictive-crime-analysis-first_prototype/edit/main/crime_prediction.py) - folder containing the hyperparameter tuning results (accuracy score & mean squared error) at each iteration of different machine learning models.
- Crime Prediction is using regression models; Decision Tree Regression and XGBoost Regression for predicting the number of crimes for particular crime head mentioned in FIR dataset. Using hyperparameter tuning outputs, the output is toggled between the abovementioned models based on their accuracy scores and mean squared error. The model is able to achieve almost 99% accuracy scores.
- Criminal Prediction is using Random Forest Classifier to predict the criminal behavior based on certain parameters like crime history, that helps in identifying the type of crime that can be committed by the criminal. This is currently a low accuracy model due to discrepencies faced for data quality and can be improved by further upgrading the data.
- Criminal Prediction Original is a heavier and more accurate model of criminal prediction which uses a similar approach as the previously mentioned point, but it refers to three distinct datasets; `VictimInfoDetails, FIR_Details_Data, Accused_Person_Info`. This helps in analysing the socio-economic background, age, profession, caste, etc. of the criminal and the intended motives as well as injuries incurred by the criminal.
- Districtwise crimes uses Linear Regression, Decision Tree Regession and Random Forest Regression for providing an estimated count of crimes for particular district in upcoming year. Hyperparameter tuning is used on accuracy scores & mean-squared-error to produce the most accurate count of crimes.

**Deployment Plan AI**

- [Deployment Plan]([https://github.com/k-chuang/kaggle-sf-crime/blob/master/cv_results](https://github.com/Leena2403/predictive-crime-analysis-first_prototype/edit/main/DeploymentPlan.py)
- Clustering of the crime heads is achieved by approaching K-means clustering. A thorough elbow-analysis is conducted in order to retrieve the ideal cluster size, which came out to be 18 in this specific case. A new dataset which contains the crime head corresponding to its cluster is created and stored for ease of access namely cluster_dict. Using clustering information different prompts have been stored in an array which has been using supportive prompts from pre-existing GenAI models; ChatGPT 3.5 Turbo. API approaches were made, however, it couldn't be successfully deployed due to the current upgradation discrepencies from the organisations. However, API based services can be still integrated in the current model, once the services resume. Till then the self-built array provides a comprehensive solution to each and every clustered crimes.
- Each deployment plan is provided for each beat that is chosen by the user and is flexible enough to provide a deployment plan for any range of locations.
- Each plan has a group of suggestions which not only provides the needful information for the police but also suggests the interactive activities that are being needed to involve the community and educate the potential victims hence spreading awareness, providing a holistic approach to the intended audience.

## Dataset
Dataset contains incidents derived from KSP Crime Incident Reporting system. The data ranges from **2016 to 2024** (~8 years worth of data). 

## Interface
- The whole interface has been created using Streamlit. The functions from jupyter notebook and prediction analysis have been re-used and made compatible for streamlit background. Six different categories of analysis has been provided `District Analysis, Crime Analysis, Time Analysis, Criminal Analysis, Victim Analysis, Beat/Police Analysis`. For each of the category, comprehensive and useful analysis, prediction and maps have been implemented.
- All the images have been taken from Unsplash for the use case in our project.


#### Heatmap of districts given category of crime
![](Visualizations/dist_heat_map.png?raw=true)

#### Confidence Matrix for criminals based on the crime and location selected
![](Visualizations/confidence%20matrix.png?raw=true)

#### Bar Graph of Top Crimes per District
![](Visualisations/crime_per_year_district.jpg?raw=true)

#### Histogram of Crimes
![](Visualisations/hist_crimes.png?raw=true)

#### Victim Details 
![](Visualisations/victim%20details.png)










