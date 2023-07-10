"""
Given two strings a and b. The task is to find if a string 'a' can be obtained by rotating another string 'b' by 2 places.
Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. In the next two line are two string a and b.

Output:
For each test case in a new line print 1 if the string 'a' can be obtained by rotating string 'b' by two places else print 0.

Constraints:
1 <= T <= 50
1 <= length of a, b < 100

Example:
Input:
2
amazon
azonam
geeksforgeeks
geeksgeeksfor

Output:
1
0

Explanation:
Testcase 1: amazon can be rotated anti-clockwise by two places, which will make it as azonam.
Testcase 2: geeksgeeksfor can't be formed by any rotation from the given word geeksforgeeks.
"""
t = int(input())                                    # test case input
for i in range(1, t + 1):                           # range
    s = input()                                     # Given Input
    s1 = input()                                    # Checking Input
    if s1 == (s[2:] + s[:2]) or (s[-2:] + s[:-2]):  # First Condition is clock-wise,Second Condition Anti-clockwise
        print(1)                                    # if it is done print '1'
    else:
        print(0)                                    # else print '0'

