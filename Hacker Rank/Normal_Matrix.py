# Matrix
# Print the matrix in Normal way
"""
For a given Row,col values print the matrix
eg:
3X3     4X4
1 2 3   1 2 3 4
4 5 6   5 6 7 8
7 8 9   9 10 11 12
        13 14 15 16
"""
Row, Col = map(int, input().split(" "))             # Input
mat = Row * Col                                     # For How many Numbers want 3X3 9 values
i = 1                                               # For counting col value
for j in range(1, mat + 1):                         # Up to n values
    if j == Col * i:                                # Col multiples are come cursor should go to nxt line
        print(j, end=" \n")
        i += 1
    else:                                           # print all values other than col multiple
        print(j, end=" ")

