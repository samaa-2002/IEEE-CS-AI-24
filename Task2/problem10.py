#Implement a guessing game where the computer generates a random number
# between 1 and 100, and the user has to guess the number.
import random
number=random.randint(1,100)
try:
    while True:
        guess = int(input("Enter number between(1-100):"))
        if guess==number:
            print("your guess is true")
            break
        elif guess<number:
           print("Number is higher! Try again")
        else :
               print("Number is lower! Try again")
except ValueError:
    print(" you should write an intger number")