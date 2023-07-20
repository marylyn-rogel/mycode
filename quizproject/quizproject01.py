#!/usr/bin/env python3

#quiz will tell the user which character they are from the new 
#puss in boots: the last wish movie
#the character options/results will be
#puss in boots, kitty softpaws, or perrito


#telling the code to run until it breaks
while True:

## Collect input from user
    last_wish = input("What would you wish for, if you had the magic star? (options: More Lives, Someone to Trust, or A Family):  ")

## using .lower and .strip to try and prevent input errors
    if last_wish.lower().strip() == "more lives":
        print("You want more lives. You must be Puss In Boots")
        break

    elif last_wish.lower().strip() == "someone to trust":
        print("You want someone to trust. You must be Kitty SoftPaws")
        break

    elif last_wish.lower().strip() == "a family":
        print("you want a family. you must be perrito")
        break
    else:
        print("sorry that is not an option. try again and choose one of the following: More Lives, Someone to Trust, or A Family!")




