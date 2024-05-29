Intro:
With pollution and global warming on the rise, the quality of air we breathe plays a crucial role in our health. Predicting air quality is a necessary step to remedy
health issues especially related to respiratory functions. The levels of pollutants in the air are recorded and published by governments. In this project I utilized such datasets to 
store, process and predict the safeness and quality of air.Research was done to collect structured csv data and semi structured datasets from Application Programming Interfaces and XML file from government datasets and was
then stored in databases for further statistical analysis such as prediction using Multiple Linear Regression algorithm to determine the air quality. If applied correctly the 
outcome of this documentation can be helpful to raise awareness on air quality among citizens and keep them safe.

requirements:
MongoDB, Docker, Postgresql, anaconda jupyter notebook.

Libraries required: 
pandas
http.client
pymongo
dagster
xml.etree.ElementTree
psycopg2

Number of datasets: 3 (API for live data, XML for unstructred historical data, CSV for structured historical data)

setting up API:
set up an account at RapidAPI here:
https://rapidapi.com/weatherbit/api/air-quality/details

Docker setup:
download docker desktop and create an yaml file like the one attached in the document

mongodb:
download mongodb free version for this project.

datasets links:
XML dataset: https://archive.ics.uci.edu/dataset/360/air+quality 
CSV dataset: https://www.kaggle.com/datasets/hansikasachdeva11/india-air-quality-data

In this project we will be extracting data from 3 different sources and integrating all together and then applying Linear regression to predict the air quality index
