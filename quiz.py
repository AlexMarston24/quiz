import random

def main():
  play_game()
def play_game():
   secretnumber=random.randint(1,100)
   attempts=0
   guessed_number = None

   print("try the guessing game")
   print("I have selected a number between 1 and 100, try to guess it")

   if guessed_number == secretnumber:

    guessed_number= int(input("enter your guess"))
    print(f"good job you have guessed the correct number in {attempts} attempts")

   elif guessed_number<secretnumber:
     print("too low try again")

   elif guessed_number>secretnumber:
     print("too high try again")
     
   else: 
     print("invalid answer, enter a different one") 

   if __name__== "__main__":
     main()
    
      