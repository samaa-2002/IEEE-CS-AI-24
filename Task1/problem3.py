#Write a Python program that takes a positive integer as input and calculates its factorial

import math

num=int(input("Enter number:"))
factorial=math.factorial(num)
print(f"The Factorial of {num} is {factorial}")