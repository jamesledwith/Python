# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:45:50 2020

@author: James
"""

import pandas as pd

#dataframe of table
df = pd.read_csv("airline.csv")
# number of elements
size_df = df.size
# display the first 5 rows
#print(df.head())

# select specific columns
df2 = pd.read_csv("airline.csv", usecols = ["UniqueCarrier", "FlightNum", "ActualElapsedTime", "CRSElapsedTime"])
size_df2 = df2.size

# select frist 10 culumns data
df3 = pd.read_csv("airline.csv", usecols = list(range(10)))
size_df3 = df3.size

df_actualElapsedColumn = pd.read_csv("airline.csv", usecols = ["ActualElapsedTime"])
size_aec = df_actualElapsedColumn.size
# display the first few columns
df_describe = df.describe()
print(df_describe)

# take out just the distance column
distance = df["Distance"]

# take out just the delay column (more of an OOP style)
delay = df.DepDelay
# gives a series where magnitude is > = 0
delay_mag = df.DepDelay[df.DepDelay >= 0] 
delay_mag_size = delay_mag.count()
# id for the max
max_delay = delay.idxmax()

print(max_delay)
# give all information about a location
max_location = df.loc[max_delay]

#gets the correlation between two columns
correlation = df.ActualElapsedTime.corr(df.CRSElapsedTime)


unique_group = df.groupby("UniqueCarrier").size().idxmax()