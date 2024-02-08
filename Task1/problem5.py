#Write a Python program that checks if a given word is a palindrome.
# A palindrome is a word that reads the same backward as forward.
word=input("Enter a word:")
half_index=int(len(word)/2)
word=word.lower()

if word[0:half_index:1]==word[half_index+1:][::-1]:
    print(f"The word '{word}' is  a palindrome")
else:
    print(f"The word '{word}' is not a palindrome")
