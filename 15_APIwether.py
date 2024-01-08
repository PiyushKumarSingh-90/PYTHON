API_KEY='007cf1373b288f507576cc72315c98c8'

import requests
import datetime

city=input("Enter the city : ")

response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=Metric")

a=response.json()
print(a)

if 'message' in a:
    print("city not found !")

else:
    print("\nCity:",city)
    print("Temperature:",a['main']['temp'],"C")
    print("Humidity:",a['main']['humidity'])
    print("Sunrise(IST):",datetime.datetime.fromtimestamp(a['sys']['sunrise']))
    print("Sunset(IST):",datetime.datetime.fromtimestamp(a['sys']['sunset']))