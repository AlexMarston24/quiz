
import random
def main():
    play_game()
    genRandomNumber()
    playerGuess()
    give_feedback()
    
def genRandomNumber():
    secretNumber = random.randint(1, 100)
    
   print("try the guessing game")
   print("I have selected a number between 1 and 100, try to guess it")
   if guessed_number == secretnumber:
def play_game():
    secretnumber=random.randint(1,100)
    attempts=0
    guessed_number = int(input("enter your guess"))
    
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

