
import random
def main():
    genRandomNumber()
    playerGuess()
    give_feedback()
    
def genRandomNumber():
    num = random.randint(1, 100)

 
def give_feedback():
    if(int(guess) > secretNumber):
        print("Too high")
    elif(int(guess) < secretNumber):
        print("Too low")
    else:
        print("Correct")
        print("1 attempt")
    if(int(guess1) > secretNumber):
        print("Too high")
    elif(int(guess1) < secretNumber):
        print("Too low")
    else:
        print("Correct")
        print("2 attempts")
    if(int(guess2) == secretNumber):
        print("Correct")
        print("3 attempts")
    else:
        print("The number is " + str(secretNumber))
        print("You didn't correctly guess the number.")
        
def playerGuess():
    guess = input("Please enter a guess of a number between 1 and 100: ")
    guess1 = input("Please enter a guess of a number between 1 and 100: ") 
    guess2 = input("Please enter a guess of a number between 1 and 100: ") 
    

if __name__ == "__main__":
    main()
