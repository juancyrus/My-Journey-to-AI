# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Input
# W3r@100a
# Output
# Valid password

import re

Password = input("Please enter your password here: ")


x = True

while x :
    if (len(Password)<6 or len(Password)>12):
        break
    elif not re.search("[a-z]",Password):
        break
    elif not re.search("[0-9]",Password):
        break
    elif not re.search("[A-z]",Password):
        break
    elif not re.search("[$#@]",Password):
        break
    elif re.search("\s",Password):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")
