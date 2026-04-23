# Write a Python program to check a triangle is valid or not 
# A triangle is valid if the sum of any two sides is greater than the third side

def sum(arg1, arg2):
    return arg1 + arg2

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))



if sum(a, b) > c and sum(b, c) > a and sum (a, c) > b:
    print("valid")
else:
    print("invalid")