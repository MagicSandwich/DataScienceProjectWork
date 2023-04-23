#importing panda for easier conversion of raw data to dataset
import pandas as pd
#importing json library
import json

#Enter filename inside of json file
file = 'uralsk'
#Reading JSON file created usig OpenWeather API
f = open('./json/'+file+'.json')

#Loading JSON file as dictionary
data = json.load(f)

#Deleting useless data
del data['coord']
#normalizing data
df = pd.json_normalize(data['list'])
df['City'] = file.capitalize()
#time = df.get('dt')
#df['dt'] = pd.to_datetime(df['dt'], unit='s') + pd.Timedelta('06:00:00')
#for i in range(len(time)):
 #   dateandtime = datetime.fromtimestamp(time[i], timezone(+timedelta(hours=6)))
 #   onlydate = dateandtime.strftime('%m-%d-%Y')
 #   onlytime = dateandtime.strftime('%H:%M:%S')
    
#export our data to CSV Dataset.
df.to_csv('csv/'+file+'.csv',index=False, header=['Date','Air Quality Index','CO','NO','NO2','O3','SO2','PM2_5','PM10','NH3','City'])

#   Air Quality Index. Possible values: 1, 2, 3, 4, 5. Where 1 = Good, 2 = Fair, 3 = Moderate, 4 = Poor, 5 = Very Poor.
#   components.co Сoncentration of CO (Carbon monoxide), μg/m3
#   components.no Сoncentration of NO (Nitrogen monoxide), μg/m3
#   components.no2 Сoncentration of NO2 (Nitrogen dioxide), μg/m3
#   components.o3 Сoncentration of O3 (Ozone), μg/m3
#   components.so2 Сoncentration of SO2 (Sulphur dioxide), μg/m3
#   components.pm2_5 Сoncentration of PM2.5 (Fine particles matter), μg/m3
#   components.pm10 Сoncentration of PM10 (Coarse particulate matter), μg/m3
#   components.nh3 Сoncentration of NH3 (Ammonia), μg/m3
