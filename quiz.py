
import random
def main():
    play_game()
 

    
def play_game():
    secretNumber = random.randint(1, 100)
    print("try the guessing game")
    print("I have selected a number between 1 and 100, try to guess it")
    guess = input("Please enter a guess of a number between 1 and 100: ")
    if(int(guess) > secretNumber):
        print("Too high")
    elif(int(guess) < secretNumber):
        print("Too low")
    else:
        print("Correct")
        print("1 attempt")
    guess1 = input("Please enter a guess of a number between 1 and 100: ")
    if(int(guess1) > secretNumber):
        print("Too high")
    elif(int(guess1) < secretNumber):
        print("Too low")
    else:
        print("Correct")
        print("2 attempts")
    guess2 = input("Please enter a guess of a number between 1 and 100: ")
    if(int(guess2) == secretNumber):
        print("Correct")
        print("3 attempts")
    else:
        print("The number is " + str(secretNumber))
        print("You didn't correctly guess the number.")
         
if __name__ == "__main__":
    main()

