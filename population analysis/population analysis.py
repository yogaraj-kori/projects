import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

state_areas=pd.read_csv(r"C:\Users\vishw\Downloads\state-areas.csv")

state_abbv=pd.read_csv(r"C:\Users\vishw\Downloads\state-abbrevs.csv")

state_info=pd.merge(state_areas, state_abbv)



state_info.columns=['state','area','state_code']
#{'area (sq. mi)':'area','abbreviation':'state_code'}
print(state_info.head())

biggest_area=state_info["area"].max()
smallest_area=state_info["area"].min()

biggest_state=state_info[state_info["area"]==biggest_area]
smallest_state=state_info[state_info["area"]==smallest_area]

print("biggest state is \n",biggest_state)
print("smallest state is \n",smallest_state)

more_info=pd.read_csv(r"C:\Users\vishw\Downloads\state-population.csv")

more_info.columns=['state_code','ages','year','population']



more_info_1=pd.merge(more_info,state_info,on="state_code")


alabama=more_info_1[more_info_1["state"]=="Alabama"]


#overallpop=more_info_1.groupby("state_code")["population"].sum()
#print(overallpop)

alabama_under18=alabama[alabama["ages"]=="under18"]
alabama_total=alabama[alabama["ages"]=="total"]
population_under18=alabama_under18.groupby("year")["population"].mean()
population_total=alabama_total.groupby("year")["population"].mean()


fig,ax=plt.subplots(figsize=(16,8))
plt.plot(population_under18,color="red")
plt.title("Population of Under 18 for Alabama",fontsize="18")
plt.xlabel("year", fontsize="14")
plt.ylabel("population",fontsize="14")


fig,ax=plt.subplots(figsize=(16,8))
plt.plot(population_total,color="blue")
plt.title(" Total Population of Alabama",fontsize="18")
plt.xlabel("year", fontsize="14")
plt.ylabel("population",fontsize="14")




#fig=px.choropleth_mapbox(more_info_1, geojson='state', locations='population', color='year',
#                           color_continuous_scale="Viridis",
#                           range_color=(0, 12),
#                          mapbox_style="carto-positron",
#                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},                           opacity=0.5,
#                           labels={'State':'population'})

#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()

more_info_under18=more_info_1[more_info_1["ages"]=="under18"]
more_info_total=more_info_1[more_info_1["ages"]=="total"]


print("\n")
txt="group by value".center(80)
print(txt)
print("\n")

print(more_info_under18.groupby("year")["population"].sum())


print("\n")
txt="covariance table for under 18".center(80)
print(txt)
print("\n")

cov_value_under18=np.cov(more_info_under18["year"],more_info_under18["population"],bias=False)
print(cov_value_under18)


fig,ax=plt.subplots(figsize=(16,8))
plt.plot(cov_value_under18,color="blue")
plt.title(" Covariance graph under 18",fontsize="18")
plt.xlabel("year", fontsize="14")
plt.ylabel("population",fontsize="14")

print("\n")
txt="covariance table for total".center(80)
print(txt)
print("\n")

cov_value_total=np.cov(more_info_total["year"],more_info_total["population"],bias=False)
print(cov_value_total)

fig,ax=plt.subplots(figsize=(16,8))
plt.plot(cov_value_total,color="blue")
plt.title(" Covariance graph for total",fontsize="18")
plt.xlabel("year", fontsize="14")
plt.ylabel("population",fontsize="14")


print("\n")
txt="corelation table for under 18".center(80)
print(txt)
print("\n")


corr_value_under18=np.corrcoef(more_info_under18["year"],more_info_under18["population"],rowvar=True)
print(corr_value_under18)

fig,ax=plt.subplots(figsize=(16,8))
plt.plot(corr_value_under18,color="blue")
plt.title(" Correlation graph under 18",fontsize="18")
plt.xlabel("year", fontsize="14")
plt.ylabel("population",fontsize="14")

print("\n")
txt="corelation table for total".center(80)
print(txt)
print("\n")


corr_value_total=np.corrcoef(more_info_total["year"],more_info_total["population"],rowvar=True)
print(corr_value_total)

fig,ax=plt.subplots(figsize=(16,8))
plt.plot(corr_value_total,color="blue")
plt.title(" Correlation graph total",fontsize="18")
plt.xlabel("year", fontsize="14")
plt.ylabel("population",fontsize="14")


under18=sum(more_info_under18["population"])
overall=sum(more_info_total["population"])-under18


list1=[overall,under18]
list2=["above 18","under 18"]
fig, ax = plt.subplots()
ax.pie(list1, labels=list2)
plt.title("Pie chart showing above 18 and under 18 population ")


print(more_info_total.columns)
population_list=list(more_info_total.groupby("state_code")["population"].sum())

state_list=list(more_info_total.state_code.unique())
print(population_list)
print(state_list)

fig,ax=plt.subplots(figsize=(16,8))
plt.scatter(state_list, population_list )
plt.title("state populations")
plt.xlabel("states")
plt.ylabel("population in millions")
plt.show()

fig,ax=plt.subplots(figsize=(16,8))
plt.bar(state_list, population_list )
plt.title("population vs states")
plt.xlabel("states")
plt.ylabel("population in millions")
plt.show()

fig, ax = plt.subplots(figsize=(10,10))
ax.pie(population_list, labels=state_list)
plt.title("Pie chart population vs state ")

print(state_info["area"])

fig,ax=plt.subplots(figsize=(16,8))
plt.bar(state_list, population_list )
plt.bar(state_info["area"], population_list )
plt.title("population vs states")
plt.xlabel("states")
plt.ylabel("population in millions")
plt.show()
