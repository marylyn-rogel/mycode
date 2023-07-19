#!/usr/bin/env python3

#Goals: 
 #   get three guesses to choose the answer! 
# guess correct, end the loop early, 
#guess wrong, and <3 guess, try again
#GUESS WRONG AND == 3 guess, we lose

gameround = 0
while True:
    #when this loop ends, the game is over!
    gameround += 1 # same

    print('Finish the movie title, "Monty Python The Life of ______"')
    answer = input("Your guess--> ")
    
    answer= answer.lower().strip()
    # normalizing input
    #removing excess white spaces
    if answer == 'brian':
        print('correct! you guessed right')

        #end the game
        break

    elif gameround == 3:
        #three guesses, you're out!
        print("the answer is Brian. you lose")
        break

    else:
        print("Sorry, try again!")




