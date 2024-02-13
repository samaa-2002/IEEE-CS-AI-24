#Generate a random password of 8 characters, including a mix of uppercase
# letters, lowercase letters, and numbers.
import random
import string
password=""

chars = string.digits + string.ascii_letters
for x in range(8):
   password+=random.choice(chars)
print(password)