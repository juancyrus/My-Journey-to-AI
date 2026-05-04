# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

# Let name all side using alphabets so side 1 = a, side 2 = b and side 3 = c

a = int(input(" Enter the length of side 1: "))
b = int(input(" Enter the length of side 2: "))
c = int(input(" Enter the length of side 3: "))

if a == b == c:
    print("An quilateral triangle")
elif a != c and b != a and b != c:
    print(" A scalene triangle" )
else:
    print(" An isosceles traingle")
