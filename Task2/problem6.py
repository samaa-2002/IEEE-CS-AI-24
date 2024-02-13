#Write a program that asks the user for input and handles the
# possibility of the user entering a non-numeric value.
while True:
    try :
        my_input=input("Enter a number:")
        number=int(my_input)
        print(f"you entered {number}")
        break
    except ValueError:
        print ("your input isn't numeric value")
