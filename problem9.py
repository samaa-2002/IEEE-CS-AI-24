#Write a function that takes two sets as input and returns a new set
# containing the common elements.
set1_input=input("Enter elements of set 1 seperated by spaces: ")
set2_input=input("Enter elements of set 2 seperated by spaces: ")
set1=set(set1_input.split())
set2=set(set2_input.split())
commen_set=set1 & set2
if len(commen_set)>0:
  print(f"commen sets={commen_set}")
else:
    print("there is no common sets")