# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.
# Input
# Input number of rows: 3                                                                                       
# Input number of columns: 4  
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]] 

m = int(input("Provide a digit that will pass as number of rows in a two- dimensional array:" ))
n = int(input("Provide an input that will pass as number of coloumns in a two-dimensional array:"))
array = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)
    array.append(row)

print(array)
