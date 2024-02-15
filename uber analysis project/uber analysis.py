import pandas as pd
import matplotlib.pyplot as plt

uber_df=pd.read_csv(r"C:\Users\vishw\Downloads\Python-Projects-Uber-Trips-Analysis\Data\uber-raw-data-sep14.csv")

#printing head, tail, shape and info of the dataframe
#print(uber_df.tail())
#print(uber_df.head())
#print(uber_df.shape)
#print(uber_df.info)

##seperating date/time into date hour and weekday
uber_df['Date/Time']=pd.to_datetime(uber_df['Date/Time'])

uber_df['Date']=uber_df['Date/Time'].apply(lambda x:x.day)
uber_df['Hour']=uber_df['Date/Time'].apply(lambda x:x.hour)
uber_df['Weekday']=uber_df['Date/Time'].apply(lambda x:x.weekday())

print(uber_df.tail(5))

##ploting the data
fig,ax=plt.subplots(figsize=(12,6))

#plt.hist(uber_df.Date,width=0.6,bins=30,color="pink")
#plt.title("Density of trips per day",fontsize=20)
#plt.xlabel("Days",fontsize=16)
#plt.ylabel("Number of trips",fontsize=16)

#plt.hist(uber_df.Weekday, width=0.6,bins=30,color="red")
#plt.title("density per weekday")
#plt.xlabel("weekdays",color="pink")
#plt.ylabel("density",color="green")

plt.hist(uber_df.Hour, width=0.6,bins=30,color="red")
plt.title("density per Hour")
plt.xlabel("weekdays",color="pink")
plt.ylabel("density",color="green")
