ggggg
# Guess the Number
import random 
target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target (or) Quit: ")
    if (userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if (userChoice == target):
        print("You guessed it right!")
        break
    elif (userChoice < target):
        print("Too low!. Take a bigger guess...")
    else:
        print("Too high!. Take a smaller guess..")

print("--- GAME OVER ---")
    

              
# Output:

'''
Guess the target (or) Quit: 50
Too high!. Take a smaller guess..
Guess the target (or) Quit: 40
Too high!. Take a smaller guess..
Guess the target (or) Quit: 35 
Too high!. Take a smaller guess..
Guess the target (or) Quit: 25
Too high!. Take a smaller guess..
Guess the target (or) Quit: 15
Too high!. Take a smaller guess..
Guess the target (or) Quit: 10
Too high!. Take a smaller guess..
Guess the target (or) Quit: 4
Too low!. Take a bigger guess...
Guess the target (or) Quit: 8
Too high!. Take a smaller guess..
Guess the target (or) Quit: 6
Too high!. Take a smaller guess..
Guess the target (or) Quit: 5
You guessed it right!
--- GAME OVER ---

'''








