#Create a program that reads a text file, counts the occurrences
# of each word, and prints the results.

import string


def remove_punctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))


with open('../sample.txt') as file:
    my_file = file.read()
    words = my_file.split()

    word_count = {}

    for word in words:
        word = remove_punctuation(word)
        if word:
            word_count[word] = word_count.get(word, 0) + 1


    for word, count in word_count.items():
        print(f"Occurrences of '{word}': {count}")
