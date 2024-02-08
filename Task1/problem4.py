#Write a Python program that takes a sentence as input and reverses the order of
# words in the sentence.
sentence=input("Enter a sentence:")
words=sentence.split()
reversed_sentence=' '.join(reversed(words))
print(f"Reversed sentence={reversed_sentence}")
