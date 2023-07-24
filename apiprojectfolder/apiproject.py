#!/usr/bin/python3

import requests


# Step 1: Make a request to the Bored API to get a random activity suggestion
data =requests.get('https://www.boredapi.com/api/activity/')


# Step 2: Check if the request was successful and the response contains valid data
if data.status_code == 200:
    #usually do the try/except
    # Step 3: Extract the activity suggestion from the JSON response
    activity = data.json()

print("Suggested Activity:", activity)

#else:
    # Step 4: If the request failed, print an error message
 #   print("Failed to retrieve activity suggestion. Please try again later.")

