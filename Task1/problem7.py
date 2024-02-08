#Write a Python program that takes a positive integer as input and finds its
# prime factors.
import math
factors = []
prime_factors = []
num = int(input("Enter number:"))

for i in range(2, num + 1):
    if num % i == 0:
        factors.append(i)

for i in factors:
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i  not in prime_factors:
        prime_factors.append(i)

print(f"Prime factors:{prime_factors}")

