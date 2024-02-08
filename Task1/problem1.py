# Write a program that takes any numbers from user terminates if user enters -1
# then prints largest and smallest number
smallest = float('inf')
largest = float('-inf')
num = int(input("enter num (-1 to terminate):"))
while num != -1:
    num = int(input("enter num:"))
    smallest = min(smallest, num)
    largest = max(largest, num)


print(f"smallest num={smallest}")
print(f"largest num={largest}")