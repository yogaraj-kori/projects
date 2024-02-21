import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import calendar as cal

my_dict={}
apple=pd.read_csv(r"C:\Users\vishw\Downloads\AAPL.csv",usecols=['Date','Close','Volume'])
txt="Apple".center(80)
print(txt)
print("\n")
#print(apple)
#print(apple.columns)

apple["Weighted average"]=apple["Close"]*apple["Volume"]

#print(apple.head())

overweightavg=apple["Weighted average"].mean()
print("overall mean is ",overweightavg)

medianval=apple["Close"].median()
mediandate=apple[apple["Close"]==medianval]
print("the median value is ",medianval)
print("median date is \n \n",mediandate["Date"])

variance_value=apple["Close"].var()
print(" the variance value is ",variance_value)

std_deviation=apple["Close"].std()
print("the standard deviation of the data is ",std_deviation)
print("\n\n")
txt="Microsoft".center(80)
print(txt)
print("\n")

microsoft=pd.read_csv(r"C:\Users\vishw\Downloads\MSFT.csv",usecols=["Date","High","Low","Close"])

#print(microsoft.columns)
#print(microsoft.head())

highest_high=microsoft["High"].max()
lowest_low=microsoft["Low"].min()
highest_highdate=microsoft[microsoft["High"]==highest_high]
lowest_lowdate=microsoft[microsoft["Low"]==lowest_low]

print("highest high is ",highest_high)
print("highest high date is ",highest_highdate["Date"])
print("lowest low is ",lowest_low)
print("lowest low date is ",lowest_lowdate["Date"])

print("\n")
txt="Covariance".center(80)
print(txt)
print("\n")

cov_value=np.cov(apple["Close"],microsoft["Close"],bias=False)
print(" The covariance table is \n")
print(cov_value)
print("\n")
print("the values on the diagonal is ",cov_value.diagonal())

print("\n")
txt="Corelation".center(80)
print(txt)
print("\n")

corr_value=np.corrcoef(apple["Close"],microsoft["Close"],rowvar=True)
print("the correlation coefficient is \n")
print(corr_value)
print("\n")
print("the values on the diagonals are ", corr_value.diagonal())

##plotting the graphs
apple["Date"]=pd.to_datetime(apple["Date"])

apple["Month"]=apple["Date"].apply(lambda x:x.month)
apple["Month"]=apple["Month"].apply(lambda x:cal.month_abbr[x])

microsoft["Date"]=pd.to_datetime(microsoft["Date"])

microsoft["Month"]=microsoft["Date"].apply(lambda x:x.month)
microsoft["Month"]=microsoft["Month"].apply(lambda x:cal.month_abbr[x])


apple_1=apple.groupby("Month",as_index=False,sort=True)


microsoft_1=microsoft.groupby("Month",as_index=False,sort=True)



fig,ax=plt.subplots(figsize=(12,6))
plt.bar(apple_1.first()["Month"],apple_1.first()["Close"],width=0.6,color="red")
plt.title(" Apple Closing data per month ")
plt.xlabel("Months")
plt.ylabel("Closing values")


fig,ax=plt.subplots(figsize=(12,6))
plt.bar(microsoft_1.first()["Month"],microsoft_1.first()["Close"],width=0.6,color="blue")
plt.title(" Apple Closing data per month ")
plt.xlabel("Months")
plt.ylabel("Closing values")

#fig,ax=plt.subplots(figsize=(20,20))
#ax=apple_1.plot(x=apple_1.first()["Month"],y=apple_1.first()["Close"],label="Apple closing",color="red")
