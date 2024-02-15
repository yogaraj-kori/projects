import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


yearly_deaths=pd.read_csv(r"C:\Users\vishw\Downloads\Python-Projects-The-Discovery-of-Handwashing\Data\yearly_deaths_by_clinic.csv")
#print head, tail, shape and info of the data set
#print(yearly_deaths.head())
#print(yearly_deaths.tail())
#print(yearly_deaths.shape)
#print(yearly_deaths.info)


##grouping by data
#print(yearly_deaths.groupby("clinic")["deaths"].sum())
#print(yearly_deaths.groupby("year")["deaths"].sum())

##overall deaths
#print("deaths",yearly_deaths["deaths"].sum())

##overall births
#print("births",yearly_deaths["births"].sum())

##differences overall
#print("difference between births and deaths",yearly_deaths["births"].sum()-yearly_deaths["deaths"].sum())

yearly_deaths["ratio"]=yearly_deaths["deaths"]/yearly_deaths["births"]
#print(yearly_deaths["ratio of birth and death"])


yearly_deaths["percentage"]=(yearly_deaths["deaths"]/yearly_deaths["births"])*100

#print(yearly_deaths)

clinic1=yearly_deaths[yearly_deaths["clinic"]=="clinic 1"]
clinic2=yearly_deaths[yearly_deaths["clinic"]=="clinic 2"]

#print(clinic1)
#print(clinic2)


fig,ax=plt.subplots(figsize=(12,6))
plt.bar(clinic1.year, clinic1.deaths,width=0.6,color="red")
plt.title("number of deaths in clinic 1",color="red",fontsize=20)
plt.xlabel("years",color="red",fontsize=18)
plt.ylabel("number of deaths",color="red",fontsize=18)

fig,ax=plt.subplots(figsize=(12,6))
plt.bar(clinic2.year, clinic2.deaths,width=0.6,color="red")
plt.title("number of deaths in clinic 2",color="red",fontsize=20)
plt.xlabel("years",color="red",fontsize=18)
plt.ylabel("number of deaths",color="red",fontsize=18)


ax=clinic1.plot(x="year",y="percentage",label="clinic1",color="red")
clinic2.plot(x="year",y="percentage",label="clinic 2",ax=ax,color="blue")

monthly_df=pd.read_csv(r"C:\Users\vishw\Downloads\Python-Projects-The-Discovery-of-Handwashing\Data\monthly_deaths.csv")
#print(monthly_df.head())
monthly_df["ratio"]=monthly_df["deaths"]/monthly_df["births"]
monthly_df["percentage"]=(monthly_df["deaths"]/monthly_df["births"])*100


##changing the data type of date
monthly_df.dtypes
monthly_df["date"]=pd.to_datetime(monthly_df["date"])
#print(monthly_df.head())

##label the date at which handwashing started
start_handwash=pd.to_datetime("1847-06-01")

before_handwashing=monthly_df[monthly_df["date"]<start_handwash]
after_handwashing=monthly_df[monthly_df["date"]>=start_handwash]

print(before_handwashing.head())
print(after_handwashing.head())

fig,ax=plt.subplots(figsize=(20,20))
ax=before_handwashing.plot(x="date",y="percentage",label="before handwashing",color="red")
after_handwashing.plot(x="date",y="percentage",ax=ax,label="after handwashing",color="green")

##getting to know how much less deaths were there after handwashing
before_ratio=before_handwashing["percentage"].mean()
after_ratio=after_handwashing["percentage"].mean()

mean_diff=before_ratio-after_ratio
print("the percentage of less deaths after handwashing was\n",mean_diff)