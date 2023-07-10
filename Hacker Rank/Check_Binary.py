# ***************Solved****************
"""
Given a non-empty sequence of characters, return true if sequence is Binary, else return false
Input:
No of test cases as T and Next Line consists of T inputs
Output:

Your function should return true str is binary, else false

Constraints:
1 <=T<= 50
1 <=Length of str<= 10000

Example:
Input:
2
101
75
Output:
1
0
"""

"""
def check_Binary(a):
    s = ["0", "1"]
    count = 0
    for i in a:
        if i in s:
            count += 1
        else:
            return False
    if count == len(a):
        True


T = int(input())
for i in range(1, T + 1):
    Num = int(input())
    print(check_Binary(str(Num)))
"""


# 1 way
def binary(n):
    b = "10"
    count = 0
    for i in n:
        if i not in b:
            count = 1
            break
    if count:
        return "False"
    return "True"


l1 = [100, 79791, 828, 4689, 8970,0000]
for i in l1:
    print(binary(str(i)))