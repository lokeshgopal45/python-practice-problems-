"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the inpu  string is valid.
An
input
string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Examples
1:
Input: s = "()"   Input: s = "()[]{}"  Input: s = "(]"
Output: True      Output:True          Output:False
"""
str = "{{[]}}"
A = str.count('(')
B = str.count('{')
C = str.count('[')
A1 = str.count(')')
B1 = str.count('}')
C1 = str.count(']')
"""
a, b, c, d = 0, 0, 0, 0
if str.count('(') == str.count(')'):
    a += 1
elif str.count('[') == str.count(']'):
    b += 1
elif str.count('{') == str.count('}'):
    c += 1
else:
    d += 1
"""
print(A, B, C)
print(A1,B1,C1)
if ('(' in str and A==A1) or ('[' in str and B==B1) or ('{' in str and C==C1):
    print(True)
else:
    print(False)