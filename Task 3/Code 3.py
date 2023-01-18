import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
%matplotlib inline
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import datetime as dt

read_US_dataset = pd.read_csv('US_Accidents_Dec20.csv')
df = pd.DataFrame(read_US_dataset )

df.drop(['End_Lat', 'End_Lng', 'Number', 'Wind_Chill(F)','Precipitation(in)'], axis=1, inplace=True)
df.dropna(axis=0)

plt.figure(figsize =(10,5))

df.groupby(['Sunrise_Sunset'])['Severity'].size().sort_values(ascending=False).plot.pie()

df['Start_Time']= pd.to_datetime(df['Start_Time'] ) df['hour']= df['Start_Time'].dt.hour
df['year']= df['Start_Time'].dt.year
df['month']= df['Start_Time'].dt.month
df['week']= df['Start_Time'].dt.week
#df['day']= df['Start_Time'].dt.weekday_name
df['quarter']= df['Start_Time'].dt.quarter
df['time_zone']= df['Start_Time'].dt.tz
df['time']= df['Start_Time'].dt.time

plt.figure(figsize =(10,5))

df.groupby(['year']).size().sort_values(ascending=True).plot.bar() plt.figure(figsize =(15,5))
df.groupby(['month']).size().plot.bar()

plt.title('Number of accidents/month')
plt.ylabel('Avg number of accidents')

dd = df['month']
dd['m'] = df['year']

plt.figure(figsize =(10,5))

df.groupby(['hour']).size().plot.bar()
plt.title('At which hour of day accidents happen')
plt.ylabel('count of accidents')

df['day_zone'] = pd.cut((df['hour']),bins=(0,6,12,18,24), labels=['night', 'morning', 'afternoon', 'evening'])
plt.figure(figsize =(10,5))

df.groupby(['day_zone']).size().plot.bar()