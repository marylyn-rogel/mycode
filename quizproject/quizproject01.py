#!/usr/bin/env python3

#quiz will tell the user which character they are from the new 
#puss in boots: the last wish movie
#the character options/results will be
#puss in boots, kitty softpaws, or perrito



## Collect input from user
last_wish = input("What would you wish for, if you had the magic star? (options: More Lives, Someone to Trust, or A Family):  ")

## using .lower and .strip to try and prevent input errors
if last_wish.lower().strip() == "more lives":
    print("You want more lives. You must be Puss In Boots")

elif last_wish.lower().strip() == "someone to trust":
    print("You want someone to trust. You must be Kitty SoftPaws")

elif last_wish.lower().strip() == "a family":
    print("you want a family. you must be perrito")

else: 
    print("sorry. try again!")




