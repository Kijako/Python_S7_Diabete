## About this project
This project was realized step by step. We have done several successive tasks to carry out our study :

Familiarization with the database, understanding the dataset
Data cleaning
Visualization of the database, with simple and more complex graphs
Implementation of a machine learning algorithm
Creation of an API using Flask and bootstrap so that a user can use the ML model with his own data
Quick presentation of the DB
The dataset represents 10 years (1999-2008) of clinical care at 130 US hospitals and integrated delivery networks. It includes over 50 features representing patient and hospital outcomes. Information was extracted from the database for encounters that satisfied the following criteria :

It is an inpatient encounter (a hospital admission)
It is a diabetic encounter, that is, one during which any kind of diabetes was entered to the system as a diagnosis
The length of stay was at least 1 day and at most 14 days
Laboratory tests were performed during the encounter
Medications were administered during the encounter
This data has been prepared to analyze factors related to readmission as well as other outcomes pertaining to patients with diabetes.

## How does the API work ?
This application is composed of 4 main parts :

Home : In this section, you will find all the general information necessary to understand how our API works and the general composition of the database

Dashboard : This section is reserved for the study of the database, you have access to several visualizations of the database, which will help you understand how the database is structured and how it can be useful to us

Prediction : This section will allow you to estimate if a patient is at risk of being readmitted to the hospital using the data you have. This data is then analyzed using a machine learning algorithm that we have trained with the database provided

Result : This page simply provides you with the estimated readmission of the patient based on the parameters entered.
