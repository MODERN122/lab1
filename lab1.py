import requests
import json
import sqlite3
'''
url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history'
params = {
    'aggregateHours':1,
    'startDateTime':'2019-06-13T00:00:00',
    'endDateTime':'2019-06-13T09:00:00',
    'unitGroup':'metric',
    'dayStartTime':'0:0:00',
    'dayEndTime':'0:0:00',
    'location':'Volgograd,Russia',
    'key':'I3D60I88UB6KPSDAVGK38HNP5',
    'contentType':'json'
}

data = requests.get(url, params).json()
'''
data = {
  "columns": {
    "wdir": {
      "id": "wdir",
      "name": "Wind Direction",
      "type": 2,
      "unit": None
    },
    "latitude": {
      "id": "latitude",
      "name": "Latitude",
      "type": 2,
      "unit": None
    },
    "cloudcover": {
      "id": "cloudcover",
      "name": "Cloud Cover",
      "type": 2,
      "unit": "%"
    },
    "mint": {
      "id": "mint",
      "name": "Minimum Temperature",
      "type": 2,
      "unit": "degC"
    },
    "datetime": {
      "id": "datetime",
      "name": "Date time",
      "type": 3,
      "unit": None
    },
    "precip": {
      "id": "precip",
      "name": "Precipitation",
      "type": 2,
      "unit": "mm"
    },
    "dew": {
      "id": "dew",
      "name": "Dew Point",
      "type": 2,
      "unit": "degC"
    },
    "humidity": {
      "id": "humidity",
      "name": "Relative Humidity",
      "type": 2,
      "unit": "%"
    },
    "precipcover": {
      "id": "precipcover",
      "name": "Precipitation Cover",
      "type": 2,
      "unit": "%"
    },
    "longitude": {
      "id": "longitude",
      "name": "Longitude",
      "type": 2,
      "unit": None
    },
    "info": {
      "id": "info",
      "name": "Info",
      "type": 1,
      "unit": None
    },
    "temp": {
      "id": "temp",
      "name": "Temperature",
      "type": 2,
      "unit": "degC"
    },
    "address": {
      "id": "address",
      "name": "Address",
      "type": 1,
      "unit": None
    },
    "maxt": {
      "id": "maxt",
      "name": "Maximum Temperature",
      "type": 2,
      "unit": "degC"
    },
    "visibility": {
      "id": "visibility",
      "name": "Visibility",
      "type": 2,
      "unit": "km"
    },
    "wspd": {
      "id": "wspd",
      "name": "Wind Speed",
      "type": 2,
      "unit": "kph"
    },
    "resolvedAddress": {
      "id": "resolvedAddress",
      "name": "Resolved Address",
      "type": 1,
      "unit": None
    },
    "heatindex": {
      "id": "heatindex",
      "name": "Heat Index",
      "type": 2,
      "unit": "degC"
    },
    "weathertype": {
      "id": "weathertype",
      "name": "Weather Type",
      "type": 1,
      "unit": None
    },
    "snowdepth": {
      "id": "snowdepth",
      "name": "Snow Depth",
      "type": 2,
      "unit": "cm"
    },
    "sealevelpressure": {
      "id": "sealevelpressure",
      "name": "Sea Level Pressure",
      "type": 2,
      "unit": "Pa"
    },
    "name": {
      "id": "name",
      "name": "Name",
      "type": 1,
      "unit": None
    },
    "wgust": {
      "id": "wgust",
      "name": "Wind Gust",
      "type": 2,
      "unit": "kph"
    },
    "conditions": {
      "id": "conditions",
      "name": "Conditions",
      "type": 1,
      "unit": None
    },
    "windchill": {
      "id": "windchill",
      "name": "Wind Chill",
      "type": 2,
      "unit": "degC"
    }
  },
  "remainingCost": 2,
  "queryCost": 10,
  "locations": {
    "Volgograd,Russia": {
      "stationContributions": None,
      "values": [
        {
          "wdir": 70.0,
          "temp": 27.0,
          "maxt": 27.0,
          "visibility": 10.0,
          "wspd": 21.6,
          "datetimeStr": "2019-06-13T00:00:00+04:00",
          "heatindex": 26.3,
          "cloudcover": 0.0,
          "mint": 27.0,
          "datetime": 1560384000000,
          "precip": 0.0,
          "weathertype": None,
          "snowdepth": None,
          "sealevelpressure": None,
          "dew": 6.0,
          "humidity": 26.25,
          "precipcover": None,
          "wgust": None,
          "conditions": "Clear",
          "windchill": None,
          "info": None
        },
        {
          "wdir": 70.0,
          "temp": 26.0,
          "maxt": 26.0,
          "visibility": 10.0,
          "wspd": 21.6,
          "datetimeStr": "2019-06-13T01:00:00+04:00",
          "heatindex": None,
          "cloudcover": 0.0,
          "mint": 26.0,
          "datetime": 1560387600000,
          "precip": 0.0,
          "weathertype": None,
          "snowdepth": None,
          "sealevelpressure": None,
          "dew": 6.0,
          "humidity": 27.84,
          "precipcover": None,
          "wgust": None,
          "conditions": "Clear",
          "windchill": None,
          "info": None
        },
        {
          "wdir": 110.0,
          "temp": 23.0,
          "maxt": 23.0,
          "visibility": 10.0,
          "wspd": 14.4,
          "datetimeStr": "2019-06-13T02:00:00+04:00",
          "heatindex": None,
          "cloudcover": 0.0,
          "mint": 23.0,
          "datetime": 1560391200000,
          "precip": 0.0,
          "weathertype": None,
          "snowdepth": None,
          "sealevelpressure": None,
          "dew": 6.0,
          "humidity": 33.32,
          "precipcover": None,
          "wgust": None,
          "conditions": "Clear",
          "windchill": None,
          "info": None
        },
        {
          "wdir": 80.0,
          "temp": 23.0,
          "maxt": 23.0,
          "visibility": 10.0,
          "wspd": 14.4,
          "datetimeStr": "2019-06-13T03:00:00+04:00",
          "heatindex": None,
          "cloudcover": 0.0,
          "mint": 23.0,
          "datetime": 1560394800000,
          "precip": 0.0,
          "weathertype": None,
          "snowdepth": None,
          "sealevelpressure": None,
          "dew": 7.0,
          "humidity": 35.69,
          "precipcover": None,
          "wgust": None,
          "conditions": "Clear",
          "windchill": None,
          "info": None
        },
        {
          "wdir": 80.0,
          "temp": 21.0,
          "maxt": 21.0,
          "visibility": 10.0,
          "wspd": 14.4,
          "datetimeStr": "2019-06-13T04:00:00+04:00",
          "heatindex": None,
          "cloudcover": 0.0,
          "mint": 21.0,
          "datetime": 1560398400000,
          "precip": 0.0,
          "weathertype": None,
          "snowdepth": None,
          "sealevelpressure": None,
          "dew": 7.0,
          "humidity": 40.32,
          "precipcover": None,
          "wgust": None,
          "conditions": "Clear",
          "windchill": None,
          "info": None
        },
        {
          "wdir": 80.0,
          "temp": 21.0,
          "maxt": 21.0,
          "visibility": 10.0,
          "wspd": 14.4,
          "datetimeStr": "2019-06-13T05:00:00+04:00",
          "heatindex": None,
          "cloudcover": 0.0,
          "mint": 21.0,
          "datetime": 1560402000000,
          "precip": 0.0,
          "weathertype": None,
          "snowdepth": None,
          "sealevelpressure": None,
          "dew": 7.0,
          "humidity": 40.32,
          "precipcover": None,
          "wgust": None,
          "conditions": "Clear",
          "windchill": None,
          "info": None
        },
        {
          "wdir": 80.0,
          "temp": 22.0,
          "maxt": 22.0,
          "visibility": 10.0,
          "wspd": 14.4,
          "datetimeStr": "2019-06-13T06:00:00+04:00",
          "heatindex": None,
          "cloudcover": 0.0,
          "mint": 22.0,
          "datetime": 1560405600000,
          "precip": 0.0,
          "weathertype": None,
          "snowdepth": None,
          "sealevelpressure": None,
          "dew": 8.0,
          "humidity": 40.6,
          "precipcover": None,
          "wgust": None,
          "conditions": "Clear",
          "windchill": None,
          "info": None
        },
        {
          "wdir": 360.0,
          "temp": 24.0,
          "maxt": 24.0,
          "visibility": 10.0,
          "wspd": 10.8,
          "datetimeStr": "2019-06-13T07:00:00+04:00",
          "heatindex": None,
          "cloudcover": 0.0,
          "mint": 24.0,
          "datetime": 1560409200000,
          "precip": 0.0,
          "weathertype": None,
          "snowdepth": None,
          "sealevelpressure": None,
          "dew": 10.0,
          "humidity": 41.17,
          "precipcover": None,
          "wgust": None,
          "conditions": "Clear",
          "windchill": None,
          "info": None
        },
        {
          "wdir": 50.0,
          "temp": 28.0,
          "maxt": 28.0,
          "visibility": 10.0,
          "wspd": 10.8,
          "datetimeStr": "2019-06-13T08:00:00+04:00",
          "heatindex": 27.2,
          "cloudcover": 0.0,
          "mint": 28.0,
          "datetime": 1560412800000,
          "precip": 0.0,
          "weathertype": None,
          "snowdepth": None,
          "sealevelpressure": None,
          "dew": 10.0,
          "humidity": 32.49,
          "precipcover": None,
          "wgust": None,
          "conditions": "Clear",
          "windchill": None,
          "info": None
        },
        {
          "wdir": 70.0,
          "temp": 31.0,
          "maxt": 31.0,
          "visibility": 10.0,
          "wspd": 14.4,
          "datetimeStr": "2019-06-13T09:00:00+04:00",
          "heatindex": 29.4,
          "cloudcover": 0.0,
          "mint": 31.0,
          "datetime": 1560416400000,
          "precip": 0.0,
          "weathertype": None,
          "snowdepth": None,
          "sealevelpressure": None,
          "dew": 9.0,
          "humidity": 25.55,
          "precipcover": None,
          "wgust": None,
          "conditions": "Clear",
          "windchill": None,
          "info": None
        }
      ],
      "id": "Volgograd,Russia",
      "address": "?????????, ????? ??????????? ?????, ??????",
      "name": "?????????, ????? ??????????? ?????, ??????",
      "index": 0,
      "latitude": 48.7041,
      "longitude": 44.4518,
      "distance": 0.0,
      "time": 0.0,
      "currentConditions": None,
      "alerts": None
    }
  }
}
#print(data['locations']['Volgograd,Russia']['values'])

with sqlite3.connect('test.db') as connection:
    c = connection.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS weather
             (date_time text, temperature real, wind_speed real, visibility real, humidity real, dew real)''')

    # Insert a row of data
    for item in data['locations']['Volgograd,Russia']['values']:
        c.execute("INSERT INTO weather VALUES (?,?,?,?,?,?)", (item['datetime'], item['temp'], item['wspd'], item['visibility'], item['humidity'], item['dew']))

    for row in c.execute('SELECT * FROM weather ORDER BY date_time'):
        print(row)

