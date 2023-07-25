#!/usr/bin/env python3


#use this to access web services
import requests

#standard library, comes installed with python
import datetime


url = "http://api.open-notify.org/iss-now.json"


#send a GET request (read data from the URL)
response=requests.get(url)

    #this of a "response" as a box full of of data
data=response.json()

lon=data


# SOLUTION TO PART 2

lon= data["iss_position"]["longitude"]
lat= data["iss_position"]["latitude"]
ts = data["timestamp"]

new_ts=datetime.datetime.fromtimestamp(ts)

print("CURRENT LOCATION OF THE ISS: ")
print("Lon: ", lon)
print("Lat: ", lat)
print(new_ts)




