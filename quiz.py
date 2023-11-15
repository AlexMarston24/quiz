import random 
def main():
    genRandomNumber()
    playerGuess()
def genRandomNumber():
    num = random.randint(1, 100)
def playerGuess():
    guess = input("Please enter a guess of a number between 1 and 100: ")
    guess1 = input("Please enter a guess of a number between 1 and 100: ") 
    guess2 = input("Please enter a guess of a number between 1 and 100: ") 
    
     
if __name__ == "__main__":
    main()