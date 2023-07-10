"""
Given a string S. The task is to print all permutations of a given string.

Input:
The first line of input contains an integer T, denoting the number of test cases. Each test case contains a single string S in capital letter.

Output: For each test case, print all permutations of a given string S with single space and all permutations should
be in lexicographically increasing order.

Example:
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA

Explanation:
Testcase 1: Given string ABC has permutations in 6 forms as ABC, ACB, BAC, BCA, CAB and CBA .

"""
from itertools import permutations          # import Permutations

t = int(input())                            # Number of test cases
for i in range(1, t + 1):                   # Up-to Number test cases
    string = input()                        # Take the Input from the user
    lt = []                                 # List to append all permutations of the string
    p = permutations(string)                # Generate all permutations of the given string
    lt.sort()                               # For lexicographical pattern we are going to sort the list
    for i in p:
        lt.append(i)                        # append all permutations into list
    for j in lt:                            # For printing the Each permutation
        print("".join(j), end=" ")          # join the single permutations -1
    print()                                 # After printing all the permutations go to next line -2

# Note
"""
1.If print the single permutations in list "lt" it prints like (('A' 'B' 'C'),('B' 'C' 'A')) so we are going to 
join all the elements in a single permutation 
2.After printing all the permutations of the given string we are going to take cursor next line
"""