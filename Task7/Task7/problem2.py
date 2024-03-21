def conditional_probability(event_a, event_b):
    total_a = event_a.count(1)
    total_b_given_a = 0
    for i in range(len(event_a)):
        if event_a[i] == 1 and event_b[i] == 1:
            total_b_given_a += 1
    if total_a != 0:
        prob_b_given_a = total_b_given_a / total_a
    else:
        prob_b_given_a = 0

    return prob_b_given_a



probabilities = [0, 1]
while True:
    user_input = input("Enter probabilities of event a (0 or 1): ")
    try:
        values_a = list(map(int, user_input.split()))
        if all(value in probabilities for value in values_a):
            break
        else:
            print("Invalid input only 0 and 1")
    except ValueError:
        print("Invalid Input")

while True:

    user_input = input("Enter probabilities of event b (0 or 1): ")
    try:
        values_b = list(map(int, user_input.split()))
        if all(value in probabilities for value in values_b):
            break
        else:
            print("Invalid input only 0 and 1")
    except ValueError:
        print("Invalid Input")

result = conditional_probability(values_a, values_b)
print("Conditional probability of event B given event A:", result)



