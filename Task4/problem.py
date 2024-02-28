import math


def get_numbers():
    while True:
        numbers = []
        input_string = input("Enter list of numbers separated by spaces: ")
        input_numbers = input_string.split()
        valid_input = True
        for x in input_numbers:
            try:
                number = float(x)
                numbers.append(number)
            except ValueError:
                print(f"{x} is invalid input. You must write only numbers.")
                valid_input = False
                break

        if valid_input:
            return numbers


def find_min(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    if not numbers:
        return None
    maximam = numbers[0]
    for num in numbers:
      if num > maximam:
          maximam = num
    return maximam


def find_mean(numbers):
    if not numbers:
        return None
    sum = 0
    length = 0
    for num in numbers:
        sum += num
        length += 1
    mean = sum / length
    return mean


def find_mode(numbers):
    if not numbers:
        return None

    num_counts = {}
    for num in numbers:
        num_counts[num] = num_counts.get(num, 0) + 1

    max_count = max(num_counts.values())

    modes = []
    for num, count in num_counts.items():
        if count == max_count:
            modes.append(num)
    if len(modes) == len(numbers):
        return None
    else:
        return modes


def find_median(numbers):
    if not numbers:
        return None
    length=len(numbers)
    numbers.sort()
    if length % 2 == 0:
        return (numbers[int((length/2))-1]+numbers[int(length/2)])/2
    else:
        return numbers[int(length/2)]


def find_range(numbers):
    if not numbers:
        return None
    return find_max(numbers)-find_min(numbers)


def find_variance(numbers):
    if not numbers:
        return None
    total = 0
    length = 0
    mean=find_mean(numbers)
    for num in numbers:
        total += (num - mean) ** 2
    return total/(len(numbers)-1)


def find_STD(numbers):
    std = math.sqrt(find_variance(numbers))
    return std


def find_Quariles(numbers):
    if not numbers:
        return None
    numbers.sort()
    q2=find_median(numbers)
    first_half=[]
    for x in range(0,int((len(numbers)/2))):
        first_half.append(numbers[x])
    q1=find_median(first_half)
    second_half=[]
    for x in range(int((len(numbers)/2)),len(numbers)):
        second_half.append(numbers[x])
    q3 = find_median(second_half)
    return q1, q2, q3


def find_IQR(numbers):
    quariles = find_Quariles(numbers)
    iqr = quariles[2] - quariles[0]
    return iqr

nums = get_numbers()
print(f"Min: {find_min(nums)}")
print(f"Max: {find_max(nums)}")
print(f"Mean: {find_mean(nums)}")
print(f"Mode: {find_mode(nums)}")
print(f"Median: {find_median(nums)}")
print(f"Range: {find_range(nums)}")
print(f"Variance: {find_variance(nums):.4f}")
print(f"Standard Deviation:: {find_STD(nums):.4f}")
print(f"Quartiles: {find_Quariles(nums)}")
print(f"Interquartile Range : {find_IQR(nums)}")