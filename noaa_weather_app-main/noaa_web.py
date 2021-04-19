import requests #requesting information from the website

import pandas as pd
import numpy as np
import datetime
from datetime import timedelta, date

from bs4 import BeautifulSoup as bs

import csv

# url = 'https://www.weather-forecast.com/locations/Bowie/forecasts/latest'
url = 'https://forecast.weather.gov/MapClick.php?'
url_bowie = 'lat=38.9595&lon=-76.7377'
url_baltimore = 'lat=42.6785&lon=-82.7346'
url_columbia_howard = 'lat=39.201&lon=-76.8316'
url_bell_perry_hall = 'lat=39.4087&lon=-76.4461'
url_westminister = 'lat=39.5816&lon=-77.0225'


#*************************Days******************

Day1 = str(date.today())
Day2 = str(date.today() + timedelta(days=1))
Day3 = str(date.today() + timedelta(days=2))
days = [Day1,Day2,Day3]

#create Dataframe from our list days
df_days = pd.DataFrame(days, columns = ['Date'])

#----------------------Bowie MD-----------------------
full_url_bowie = url + url_bowie
r = requests.get(full_url_bowie)

# using BS to pull data
forecast = bs(r.content, "lxml")

#************************* Low Temp******************
low_temp = forecast.findAll("p", {"class": "temp temp-low"})
LTemp = []
for i in range(3): # Python's `for` loop is a for-each.
    Temp = low_temp[i].text.split(' ',2)
    LTemp.append(Temp)
    # or whatever function of that item.
df_lowTemp = pd.DataFrame(LTemp, columns = ['temp type','temp', 'unit'])
#high_Temperature = df[1,2]
df_lowTemp['city'] = 'Bowie MD'
df_lowTemp['temp'] = df_lowTemp['temp'].astype(int)

bowie_LowTempData = pd.concat([df_lowTemp, df_days], axis=1)

bowie_LowTempData['Test'] = bowie_LowTempData['temp'].apply(lambda x: 'NO' if (x < 32) else 'YES')

l = bowie_LowTempData['Test'].tolist()

#final Decision logic
if 'NO' in l:
    take_action='NO'
else:
    take_action='YES'

bowie_LowTempData['Action'] = take_action

#*************************High Temp******************
#using BS to scrape HTML tags from websites
high_temp = forecast.findAll("p", {"class": "temp temp-high"})
HTemp = [] # adding the data to list
for i in range(3): # Python's `for` loop is a for-each.
    Temp = high_temp[i].text.split(' ',2) #spliting data into columns
    HTemp.append(Temp) # adding values of i into HTemp list

#creating a dataframe df_highTemp from the list Htemp    
df_highTemp = pd.DataFrame(HTemp, columns = ['temp type','temp', 'unit'])
df_highTemp['city'] = 'Bowie MD' #create city column
df_highTemp['temp'] = df_highTemp['temp'].astype(int) #converting 'high temp' column to int

#dataframe to merge days and high temperature
bowie_HighTempData = pd.concat([df_highTemp, df_days], axis=1)

#adding action to be taken logic
bowie_HighTempData['Test'] = bowie_HighTempData['temp'].apply(lambda x: 'NO' if (x >95) else 'YES')

#create list of to check if logic decision was met 
h = bowie_HighTempData['Test'].tolist()

#final Decision logic
if 'NO' in h:
    take_action='NO'
else:
    take_action='YES'

#adding the Action column based on the logic
bowie_HighTempData['Action'] = take_action

#union low_dataframe & high_dataframe bowie_LowTempData and bowie_HighTempData
bowie_data= bowie_LowTempData.append(bowie_HighTempData)

#removing the Test column from the final result 
bowie_weather_data = bowie_data.drop(columns=['Test'],axis = 1)

#rearranging the columns
bowie_weather_data = bowie_weather_data[['city','temp type', 'temp', 'unit', 'Date','Action']]

#sorting data by column date
bowie_weather_data_sort = bowie_weather_data.sort_values('Date')

# print(bowie_weather_data) #without sort
# print(bowie_weather_data_sort) #with sort on Date column


#----------------------Baltimore MD-----------------------

full_url_baltimore = url + url_baltimore
r = requests.get(full_url_baltimore)

# using BS to pull data
forecast = bs(r.content, "lxml")

#************************* Low Temp******************
low_temp = forecast.findAll("p", {"class": "temp temp-low"})
LTemp = []
for i in range(3): # Python's `for` loop is a for-each.
    Temp = low_temp[i].text.split(' ',2)
    LTemp.append(Temp)
    # or whatever function of that item.
df_lowTemp = pd.DataFrame(LTemp, columns = ['temp type','temp', 'unit'])
#high_Temperature = df[1,2]
df_lowTemp['city'] = 'Baltimore MD'
df_lowTemp['temp'] = df_lowTemp['temp'].astype(int)

baltimore_LowTempData = pd.concat([df_lowTemp, df_days], axis=1)

baltimore_LowTempData['Test'] = baltimore_LowTempData['temp'].apply(lambda x: 'NO' if (x < 32) else 'YES')

l = baltimore_LowTempData['Test'].tolist()

#final Decision logic
if 'NO' in l:
    take_action='NO'
else:
    take_action='YES'

baltimore_LowTempData['Action'] = take_action

#*************************High Temp******************
#using BS to scrape HTML tags from websites
high_temp = forecast.findAll("p", {"class": "temp temp-high"})
HTemp = [] # adding the data to list
for i in range(3): # Python's `for` loop is a for-each.
    Temp = high_temp[i].text.split(' ',2) #spliting data into columns
    HTemp.append(Temp) # adding values of i into HTemp list

#creating a dataframe df_highTemp from the list Htemp    
df_highTemp = pd.DataFrame(HTemp, columns = ['temp type','temp', 'unit'])
df_highTemp['city'] = 'Baltimore MD' #create city column
df_highTemp['temp'] = df_highTemp['temp'].astype(int) #converting 'high temp' column to int

#dataframe to merge days and high temperature
baltimore_HighTempData = pd.concat([df_highTemp, df_days], axis=1)

#adding action to be taken logic
baltimore_HighTempData['Test'] = baltimore_HighTempData['temp'].apply(lambda x: 'NO' if (x >95) else 'YES')

#create list of to check if logic decision was met 
h = baltimore_HighTempData['Test'].tolist()

#final Decision logic
if 'NO' in h:
    take_action='NO'
else:
    take_action='YES'

#adding the Action column based on the logic
baltimore_HighTempData['Action'] = take_action

#union low_dataframe & high_dataframe baltimore_LowTempData and baltimore_HighTempData
baltimore_data= baltimore_LowTempData.append(baltimore_HighTempData)

#removing the Test column from the final result 
baltimore_weather_data = baltimore_data.drop(columns=['Test'],axis = 1)

#rearranging the columns
baltimore_weather_data = baltimore_weather_data[['city','temp type', 'temp', 'unit', 'Date','Action']]

#sorting data by column date
baltimore_weather_data_sort = baltimore_weather_data.sort_values('Date')

# print(baltimore_weather_data) #without sort
# print(baltimore_weather_data_sort) #with sort on Date column


#----------------------Columbia MD-----------------------
full_url_columbia = url + url_columbia_howard
r = requests.get(full_url_columbia)

# using BS to pull data
forecast = bs(r.content, "lxml")

#************************* Low Temp******************
low_temp = forecast.findAll("p", {"class": "temp temp-low"})
LTemp = []
for i in range(3): # Python's `for` loop is a for-each.
    Temp = low_temp[i].text.split( ' ', 2 )
    LTemp.append(Temp)
    # or whatever function of that item.
df_lowTemp = pd.DataFrame(LTemp, columns = ['temp type','temp', 'unit'])

df_lowTemp['city'] = 'Columbia MD'

df_lowTemp['temp'] = df_lowTemp['temp'].astype(int)

columbia_LowTempData = pd.concat([df_lowTemp, df_days], axis=1)

columbia_LowTempData['Test'] = columbia_LowTempData['temp'].apply(lambda x: 'NO' if (x < 32) else 'YES')

l = columbia_LowTempData['Test'].tolist()

#final Decision logic
if 'NO' in l:
    take_action='NO'
else:
    take_action='YES'

columbia_LowTempData['Action'] = take_action

#*************************High Temp******************
#using BS to scrape HTML tags from websites
high_temp = forecast.findAll("p", {"class": "temp temp-high"})
HTemp = [] # adding the data to list
for i in range(3): # Python's `for` loop is a for-each.
    Temp = high_temp[i].text.split(' ',2) #spliting data into columns
    HTemp.append(Temp) # adding values of i into HTemp list

#creating a dataframe df_highTemp from the list Htemp    
df_highTemp = pd.DataFrame(HTemp, columns = ['temp type','temp', 'unit'])
df_highTemp['city'] = 'Columbia MD' #create city column
df_highTemp['temp'] = df_highTemp['temp'].astype(int) #converting 'high temp' column to int

#dataframe to merge days and high temperature
columbia_HighTempData = pd.concat([df_highTemp, df_days], axis=1)

#adding action to be taken logic
columbia_HighTempData['Test'] = columbia_HighTempData['temp'].apply(lambda x: 'NO' if (x >95) else 'YES')

#create list of to check if logic decision was met 
h = columbia_HighTempData['Test'].tolist()

#final Decision logic
if 'NO' in h:
    take_action='NO'
else:
    take_action='YES'

#adding the Action column based on the logic
columbia_HighTempData['Action'] = take_action

#union low_dataframe & high_dataframe columbia_LowTempData and columbia_HighTempData
columbia_data= columbia_LowTempData.append(columbia_HighTempData)

#removing the Test column from the final result 
columbia_weather_data = columbia_data.drop(columns=['Test'],axis = 1)

#rearranging the columns
columbia_weather_data = columbia_weather_data[['city','temp type', 'temp', 'unit', 'Date','Action']]

#sorting data by column date
columbia_weather_data_sort = columbia_weather_data.sort_values('Date')

# print(columbia_weather_data) #without sort
# print(columbia_weather_data_sort) #with sort on Date column


#----------------------bell_perry_hall MD-----------------------
full_url_bell_perry_hall = url + url_bell_perry_hall
r = requests.get(full_url_bell_perry_hall)

# using BS to pull data
forecast = bs(r.content, "lxml")

#************************* Low Temp******************
low_temp = forecast.findAll("p", {"class": "temp temp-low"})
LTemp = []
for i in range(3): # Python's `for` loop is a for-each.
    Temp = low_temp[i].text.split( ' ', 2 )
    LTemp.append(Temp)
    # or whatever function of that item.
df_lowTemp = pd.DataFrame(LTemp, columns = ['temp type','temp', 'unit'])

df_lowTemp['city'] = 'Bell Perry Hall MD'

df_lowTemp['temp'] = df_lowTemp['temp'].astype(int)

bell_perry_hall_LowTempData = pd.concat([df_lowTemp, df_days], axis=1)

bell_perry_hall_LowTempData['Test'] = bell_perry_hall_LowTempData['temp'].apply(lambda x: 'NO' if (x < 32) else 'YES')

l = bell_perry_hall_LowTempData['Test'].tolist()

#final Decision logic
if 'NO' in l:
    take_action='NO'
else:
    take_action='YES'

bell_perry_hall_LowTempData['Action'] = take_action

#*************************High Temp******************
#using BS to scrape HTML tags from websites
high_temp = forecast.findAll("p", {"class": "temp temp-high"})
HTemp = [] # adding the data to list
for i in range(3): # Python's `for` loop is a for-each.
    Temp = high_temp[i].text.split(' ',2) #spliting data into columns
    HTemp.append(Temp) # adding values of i into HTemp list

#creating a dataframe df_highTemp from the list Htemp    
df_highTemp = pd.DataFrame(HTemp, columns = ['temp type','temp', 'unit'])
df_highTemp['city'] = 'Bell Perry Hall MD MD' #create city column
df_highTemp['temp'] = df_highTemp['temp'].astype(int) #converting 'high temp' column to int

#dataframe to merge days and high temperature
bell_perry_hall_HighTempData = pd.concat([df_highTemp, df_days], axis=1)

#adding action to be taken logic
bell_perry_hall_HighTempData['Test'] = bell_perry_hall_HighTempData['temp'].apply(lambda x: 'NO' if (x >95) else 'YES')

#create list of to check if logic decision was met 
h = bell_perry_hall_HighTempData['Test'].tolist()

#final Decision logic
if 'NO' in h:
    take_action='NO'
else:
    take_action='YES'

#adding the Action column based on the logic
bell_perry_hall_HighTempData['Action'] = take_action

#union low_dataframe & high_dataframe bell_perry_hall_LowTempData and bell_perry_hall_HighTempData
bell_perry_hall_data= bell_perry_hall_LowTempData.append(bell_perry_hall_HighTempData)

#removing the Test column from the final result 
bell_perry_hall_weather_data = bell_perry_hall_data.drop(columns=['Test'],axis = 1)

#rearranging the columns
bell_perry_hall_weather_data = bell_perry_hall_weather_data[['city','temp type', 'temp', 'unit', 'Date','Action']]

#sorting data by column date
#bell_perry_hall_weather_data_sort = bell_perry_hall_weather_data.sort_values('Date')

# print(bell_perry_hall_weather_data) #without sort
# print(bell_perry_hall_weather_data_sort) #with sort on Date column



#----------------------westminister MD-----------------------
full_url_westminister = url + url_westminister
r = requests.get(full_url_westminister)

# using BS to pull data
forecast = bs(r.content, "lxml")

#************************* Low Temp******************
low_temp = forecast.findAll("p", {"class": "temp temp-low"})
LTemp = []
for i in range(3): # Python's `for` loop is a for-each.
    Temp = low_temp[i].text.split( ' ', 2 )
    LTemp.append(Temp)
    # or whatever function of that item.
df_lowTemp = pd.DataFrame(LTemp, columns = ['temp type','temp', 'unit'])

df_lowTemp['city'] = 'Westminister MD'

df_lowTemp['temp'] = df_lowTemp['temp'].astype(int)

westminister_LowTempData = pd.concat([df_lowTemp, df_days], axis=1)

westminister_LowTempData['Test'] = westminister_LowTempData['temp'].apply(lambda x: 'NO' if (x < 32) else 'YES')

l = westminister_LowTempData['Test'].tolist()

#final Decision logic
if 'NO' in l:
    take_action='NO'
else:
    take_action='YES'

westminister_LowTempData['Action'] = take_action

#*************************High Temp******************
#using BS to scrape HTML tags from websites
high_temp = forecast.findAll("p", {"class": "temp temp-high"})
HTemp = [] # adding the data to list
for i in range(3): # Python's `for` loop is a for-each.
    Temp = high_temp[i].text.split(' ',2) #spliting data into columns
    HTemp.append(Temp) # adding values of i into HTemp list

#creating a dataframe df_highTemp from the list Htemp    
df_highTemp = pd.DataFrame(HTemp, columns = ['temp type','temp', 'unit'])
df_highTemp['city'] = 'Westminister MD' #create city column
df_highTemp['temp'] = df_highTemp['temp'].astype(int) #converting 'high temp' column to int

#dataframe to merge days and high temperature
westminister_HighTempData = pd.concat([df_highTemp, df_days], axis=1)

#adding action to be taken logic
westminister_HighTempData['Test'] = westminister_HighTempData['temp'].apply(lambda x: 'NO' if (x >95) else 'YES')

#create list of to check if logic decision was met 
h = westminister_HighTempData['Test'].tolist()

#final Decision logic
if 'NO' in h:
    take_action='NO'
else:
    take_action='YES'

#adding the Action column based on the logic
westminister_HighTempData['Action'] = take_action

#union low_dataframe & high_dataframe westminister_LowTempData and westminister_HighTempData
westminister_data= westminister_LowTempData.append(westminister_HighTempData)

#removing the Test column from the final result 
westminister_weather_data = westminister_data.drop(columns=['Test'],axis = 1)

#rearranging the columns
westminister_weather_data = westminister_weather_data[['city','temp type', 'temp', 'unit', 'Date','Action']]

#sorting data by column date
#westminister_weather_data_sort = westminister_weather_data.sort_values('Date')

# print(westminister_weather_data) #without sort
# print(westminister_weather_data_sort) #with sort on Date column

#***************Complete Data Set************

frames = [bowie_weather_data,baltimore_weather_data,columbia_weather_data,bell_perry_hall_weather_data,westminister_weather_data]
weather_data = pd.concat(frames)


filename = str(date.today())

weather_data.to_csv(str(filename + '.csv'), index=False)
