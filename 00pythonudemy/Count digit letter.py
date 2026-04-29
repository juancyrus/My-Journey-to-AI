# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2

Word = input(str("Enter a numletter mixed word:"))
l_c = 0
d_c = 0

for char in Word:
    if char .isalpha():
        l_c += 1
    elif char .isdigit():
        d_c += 1

print(f"Letter: {l_c}")
print(f"Digit: {d_c}")


