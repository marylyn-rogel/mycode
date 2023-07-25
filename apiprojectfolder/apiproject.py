#!/usr/bin/python3

import requests

"""API Project """

#The user will press enter and the script will suggest an activity. 
#If the user likes the activity, then they can see more information about it
#Such as, participants, cost, etc.

#Step 1: retrieve the data
data =requests.get('https://www.boredapi.com/api/activity/')

# Step 1: Make a request to the Bored API to get a random activity suggestion

while True:
    try:
        print("Press 'ENTER' if you want a suggested activity! ")
        activity = data.json()
        print("Suggested Activity:", activity)
    except Exception: 
        print("Press ENTER to see a suggestion")



# Step 2: Check if the request was successful and the response contains valid data
#if data.status_code == 200:
    #usually do the try/except
#else:
    # Step 4: If the request failed, print an error message
 #   print("Failed to retrieve activity suggestion. Please try again later.")

