# *************** Partially Solved *****************
"""
Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an
integer and returns it Example 1: Input:str = 123 Output: 123

Example 2:
Input:str = 21a
Output: -1

Explanation: Output is -1 as all characters are not digit only.
"""
s1=input()
start = s1[0]
if start == "-":
    s1 = s1[1:]
    if s1.isnumeric():
        print(s1)
elif s1.isnumeric():
    print(s1)
else:
    print(-1)
