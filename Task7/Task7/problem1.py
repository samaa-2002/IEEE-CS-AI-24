#Write a Python function that takes in a list of values and returns the probability
# distribution of those values. Assume the values are discrete
def probability_distribytion(values):
    frequency={}
    probability={}
    for value in values:
        if value in frequency:
            frequency[value]+=1
        else:
            frequency[value]=1
    no_of_elements=len(values)
    for value, count in frequency.items():
        probability[value] = count / no_of_elements
    return probability

while True:
    user_input = input("Enter a list of integers separated by spaces: ")
    try:
        values = list(map(int, user_input.split()))
        print( probability_distribytion(values))
        break
    except ValueError:
        print("Invalid input.integers only")

