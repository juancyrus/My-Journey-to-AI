# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615

value = int(input("Give a number that when added to it pair and triple would result in 615:" ))
expected_results = 615
print(value + int(str(value)*2) + int(str(value)*3) == 615)

if print == 615:
    print("Success")
else:
    print("Try again")
