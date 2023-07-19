#!/usr/bin/env python3

# this line now prompts the user for input
ipchk = input("Apply an IP address: ") 

# if user set IP of gateway
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")

# if any data is provided, this will test true
elif ipchk:
    print("Looks like the IP address was set: " + ipchk) 
    # indented under if


else: # if data is NOT provided
    print("You did not provide input.") # indented under else

