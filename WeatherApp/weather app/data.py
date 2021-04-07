from bs4 import BeautifulSoup
import requests

import pandas as pd
from datetime import datetime
from datetime import timedelta, date
import plotly.graph_objects as go


import plotly.graph_objects as go

from noaa_sdk import NOAA

#--------------------Bowie MD-----------------------------

Bowie_MD_Zip = '20715'

Day_1 = str(date.today()) + 'T05:00:00-04:00'
Day_2 = str(date.today() + timedelta(days=1)) + 'T05:00:00-04:00'
Day_3 = str(date.today() + timedelta(days=2)) + 'T05:00:00-04:00'



n = NOAA()
res = n.get_forecasts(Bowie_MD_Zip, 'US',hourly=False )

df = pd.DataFrame.from_dict(res)
df['Location'] = 'Bowie MD'
Bowie_MD = df[['Location','startTime','temperature']]

#print(df)


Day1_Bowie_MD = Bowie_MD[Bowie_MD['startTime'] == Day_1]
Day2_Bowie_MD = Bowie_MD[Bowie_MD['startTime'] == Day_2]
Day3_Bowie_MD = Bowie_MD[Bowie_MD['startTime'] == Day_3]
Bowie_frames = [Day1_Bowie_MD,Day2_Bowie_MD,Day3_Bowie_MD]
Bowie_MD_Data = pd.concat(Bowie_frames, ignore_index=True)

Bowie_MD_Data['Action'] = Bowie_MD_Data['temperature'].apply(lambda x: 'Yes' if (x >=32 and x <=95) else 'NO')

#renaming column startTime

Bowie_MD_Data.rename(columns = {'startTime':'Date_Time'}, inplace = True)

#print(Bowie_MD_Data)


#----------------------Baltimore----------------------

Baltimore_Front_Street = '21202'

Day_1 = str(date.today()) + 'T05:00:00-04:00'
Day_2 = str(date.today() + timedelta(days=1)) + 'T05:00:00-04:00'
Day_3 = str(date.today() + timedelta(days=2)) + 'T05:00:00-04:00'



n = NOAA()
res = n.get_forecasts(Baltimore_Front_Street, 'US',hourly=False )

df = pd.DataFrame.from_dict(res)
df['Location'] = 'Baltimore - Front Street'
Baltimore_MD = df[['Location','startTime','temperature']]

Day1_Baltimore_MD = Baltimore_MD[Baltimore_MD['startTime'] == Day_1]
Day2_Baltimore_MD = Baltimore_MD[Baltimore_MD['startTime'] == Day_2]
Day3_Baltimore_MD = Baltimore_MD[Baltimore_MD['startTime'] == Day_3]
Baltimore_frames = [Day1_Baltimore_MD,Day2_Baltimore_MD,Day3_Baltimore_MD]
Baltimore_MD_Data = pd.concat(Baltimore_frames, ignore_index=True)

Baltimore_MD_Data['Action'] = Baltimore_MD_Data['temperature'].apply(lambda x: 'Yes' if (x >=32 and x <=95) else 'NO')

Baltimore_MD_Data.rename(columns = {'startTime':'Date_Time'}, inplace = True)


#print(Baltimore_MD_Data)


# #----------------------Columbia - Howard----------------------

Columbia_Howard = '21045'

Day_1 = str(date.today()) + 'T05:00:00-04:00'
Day_2 = str(date.today() + timedelta(days=1)) + 'T05:00:00-04:00'
Day_3 = str(date.today() + timedelta(days=2)) + 'T05:00:00-04:00'



n = NOAA()
res = n.get_forecasts(Columbia_Howard, 'US',hourly=False )

df = pd.DataFrame.from_dict(res)
df['Location'] = 'Columbia - Howard'
Columbia_MD = df[['Location','startTime','temperature']]

Day1_Columbia_MD = Columbia_MD[Columbia_MD['startTime'] == Day_1]
Day2_Columbia_MD = Columbia_MD[Columbia_MD['startTime'] == Day_2]
Day3_Columbia_MD = Columbia_MD[Columbia_MD['startTime'] == Day_3]
Columbia_frames = [Day1_Columbia_MD,Day2_Columbia_MD,Day3_Columbia_MD]
Columbia_MD_Data = pd.concat(Columbia_frames, ignore_index=True)

Columbia_MD_Data['Action'] = Columbia_MD_Data['temperature'].apply(lambda x: 'Yes' if (x >=32 and x <=95) else 'NO')
Columbia_MD_Data.rename(columns = {'startTime':'Date_Time'}, inplace = True)


#print(Columbia_MD_Data)



#----------------------Bell Air - Perry Hall----------------------

Bel_Air = '21128'

Day_1 = str(date.today()) + 'T05:00:00-04:00'
Day_2 = str(date.today() + timedelta(days=1)) + 'T05:00:00-04:00'
Day_3 = str(date.today() + timedelta(days=2)) + 'T05:00:00-04:00'



n = NOAA()
res = n.get_forecasts(Bel_Air, 'US',hourly=False )

df = pd.DataFrame.from_dict(res)
df['Location'] = 'Bell Air - Perry Hall'
Bel_Air_MD = df[['Location','startTime','temperature']]

Day1_Bel_Air_MD = Bel_Air_MD[Bel_Air_MD['startTime'] == Day_1]
Day2_Bel_Air_MD = Bel_Air_MD[Bel_Air_MD['startTime'] == Day_2]
Day3_Bel_Air_MD = Bel_Air_MD[Bel_Air_MD['startTime'] == Day_3]
Bel_Air_frames = [Day1_Bel_Air_MD,Day3_Bel_Air_MD,Day3_Bel_Air_MD]
Bel_Air_MD_Data = pd.concat(Bel_Air_frames, ignore_index=True)

Bel_Air_MD_Data['Action'] = Bel_Air_MD_Data['temperature'].apply(lambda x: 'Yes' if (x >=32 and x <=95) else 'NO')

Bel_Air_MD_Data.rename(columns = {'startTime':'Date_Time'}, inplace = True)

#print(Bel_Air_MD_Data)



#----------------------Westminister -Cockeysville----------------------

Westminister = '21158'

Day_1 = str(date.today()) + 'T05:00:00-04:00'
Day_2 = str(date.today() + timedelta(days=1)) + 'T05:00:00-04:00'
Day_3 = str(date.today() + timedelta(days=2)) + 'T05:00:00-04:00'



n = NOAA()
res = n.get_forecasts(Westminister, 'US',hourly=False )

df = pd.DataFrame.from_dict(res)
df['Location'] = 'Westminister -Cockeysville'
Westminister_MD = df[['Location','startTime','temperature']]

Day1_Westminister_MD = Westminister_MD[Westminister_MD['startTime'] == Day_1]
Day2_Westminister_MD = Westminister_MD[Westminister_MD['startTime'] == Day_2]
Day3_Westminister_MD = Westminister_MD[Westminister_MD['startTime'] == Day_3]
Westminister_frames = [Day1_Westminister_MD,Day2_Westminister_MD,Day3_Westminister_MD]
Westminister_MD_Data = pd.concat(Westminister_frames, ignore_index=True)

Westminister_MD_Data['Action'] = Westminister_MD_Data['temperature'].apply(lambda x: 'Yes' if (x >=32 and x <=95) else 'NO')

Westminister_MD_Data.rename(columns = {'startTime':'Date_Time'}, inplace = True)

#print(Westminister_MD_Data)



#--------------Mainframe Data------------------

main_frame = [Bowie_MD_Data,Baltimore_MD_Data,Columbia_MD_Data, Bel_Air_MD_Data, Westminister_MD_Data]

main_file = pd.concat(main_frame, ignore_index=True)

filename = str(date.today())

main_file.to_csv(str(filename + '.csv'), index=False)

