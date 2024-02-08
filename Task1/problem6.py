#Write a Python program that takes a positive integer as input and calculates
# the sum of all even numbers from 1 to that integer.

num=int(input("Enter a positive integer number:"))
sum=0
for i in range(num+1):
  if i%2==0:
    sum+=i

print(f"The sum of even numbers from 1 to {num} is {sum} .")