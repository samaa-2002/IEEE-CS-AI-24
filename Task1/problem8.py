#Write a Python program that takes a positive integer as input and checks whether
# it is a perfect number or not. A perfect number is a positive integer that is
# equal to the sum of its proper divisors, excluding itself
divisors = []
sum=0
num = int(input("Enter number:"))
for i in range(1, num + 1):
    if num % i == 0:
       divisors.append(i)
for i in range(len(divisors)-1):
    sum += divisors[i]
if sum==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
