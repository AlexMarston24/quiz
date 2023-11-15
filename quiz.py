import random
def main():
    give_feedback()

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

if __name__ == "__main__":
    main()

              

