#!/usr/bin/env python3

def main():
    usr_name = input("Please enter your name:\n>")
    usr_name = usr_name.title()

    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    remainder = usr_date % 12


    zodiac_signs = {
        0: "Monkey, you are sharp, smart, curious, and mischievous.",
        1: "Rooster, you are hardworking, resourceful, courageous, and talented.",
        2: "Dog, you are loyal, honest, cautious, and kind.",
        3: "Pig, you are a symbol of wealth, honesty, and practicality.",
        4: "Rat, you are artistic, sociable, industrious, charming, and intelligent.",
        5: "Ox, you are strong, thorough, determined, loyal, and reliable.",
        6: "Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.",
        7: "Rabbit, you are vigilant, witty, quick-minded, and ingenious.",
        8: "Dragon, you are talented, powerful, lucky, and successful.",
        9: "Snake, you are wise, like to work alone, and determined.",
        10: "Horse, you are animated, active, and energetic.",
        11: "Sheep, you are creative, resilient, gentle, mild-mannered, and shy."
    }

    zodiac_sign = zodiac_signs.get(remainder)
    if zodiac_sign:
        print(f"{usr_name} your zodiac sign is {zodiac_sign}")
    else:
        print("Invalid birth year, please enter a valid year.")
        main()

main()






