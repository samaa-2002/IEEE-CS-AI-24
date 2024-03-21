def conditional_probability(prior_a, prior_b, conditional_b_given_a):
    conditional_probability = (prior_a * conditional_b_given_a) / prior_b
    return conditional_probability


def get_input():
    while True:
        try:
            user_input = float(input())
            if 0 <= user_input <= 1:
                return user_input
            else:
                print("Invalid Input. Input must be between 0 and 1.")
        except ValueError:
            print("Invalid Input")


print("Enter prior probability of event A:")
prior_a = get_input()

print("Enter prior probability of event B:")
prior_b = get_input()

print("Enter conditional probability of B given A:")
conditional_b_given_a = get_input()

result = conditional_probability(prior_a, prior_b, conditional_b_given_a)
print("Probability of event A given event B:", result)
