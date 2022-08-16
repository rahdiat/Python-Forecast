import requests

parameters = {
    "lat": -6.21,
    "lon": 106.84,
    "units": "metric",
    "exclude": "minutes",
    "appid": "be7dfeb7da3ff3856fc22de66a02b653"
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    data = json.dumps(obj, sort_keys=True, indent=4)
    print(data)

listResponse = response.json()['daily']

dt_txt = []

for d in listResponse:
    time = d['temp']
    dt_txt.append(time)

tempDay = []

for d in dt_txt:
    time = d['day']
    tempDay.append(time)

dateTimes = []

for d in listResponse:
    time = d['dt']
    dateTimes.append(time)

from datetime import datetime
days = []
weekdays = []
i = 0
while i < 8:
  day = datetime.fromtimestamp(dateTimes[i], tz=None).date()
  weekday = datetime.fromtimestamp(dateTimes[i], tz=None).weekday()
  weekdays.append(weekday)
  days.append(day)
  i += 1

def forcast():
  i = 0
  d = datetime.now().date()
  weekday = int(d.strftime('%w'))
  print('Weather Forecast:')
  while i < 8:
    if weekday == 0:
      print("Sun,", days[i], ":", tempDay[i], "°C")
    elif weekday == 1:
      print("Mon,", days[i], ":", tempDay[i], "°C")
    elif weekday == 2:
      print("Tue,", days[i], ":", tempDay[i], "°C")
    elif weekday == 3:
      print("Wed,", days[i], ":", tempDay[i], "°C")
    elif weekday == 4:
      print("Thu,", days[i], ":", tempDay[i], "°C")
    elif weekday == 5:
      print("Fri,", days[i], ":", tempDay[i], "°C")
    elif weekday == 6:
      print("Sat,", days[i], ":", tempDay[i], "°C")
    else:
      weekday = -1
    weekday += 1
    i += 1

forcast()