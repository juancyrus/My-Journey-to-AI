# Write a Python program to check whether an alphabet is a vowel or consonant

import re 

alphabet = str(input("Enter an alphabet: "))

x = True

while x:
    if re.search("[aeiou]",alphabet):
        print("vowel")
    else:
        print("consonant")
    break
