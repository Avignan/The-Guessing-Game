import random

randomNumber = random.randint(1, 100)

userGuess = None

Guess = 0


while (userGuess != randomNumber):
    userGuess = int(input("Enter a number of your choice: "))
    Guess += 1
    if (userGuess == randomNumber):
        print("You have guessed the correct number!")
        print(f"Your took total of {Guess} guesses to get to the correct number")
    else:
        if(userGuess > randomNumber):
            print("You answer is incorrect! Please enter a smaller number to increase your chances of winning")
        else:
            print("You answer is incorrect! Please enter a higher number to increase your chances of winning")


with open("Hiscore.txt", "r") as f:
    hiscore = int(f.read())


if(hiscore > Guess):
    print("Bravo! You've just broken the hiscore")
    with open ("Hiscore.txt", "w") as f:
        f.write (str(Guess))
    
        