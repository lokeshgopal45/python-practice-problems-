"""
Given a string, remove spaces from it
Input: First line of the input is the number of test cases T.
And first line of test case contains a string whose spaces are to be removed.

Output:  Modified string without any space

Constraints:  Input String Length <= 1000

Example:
Input:
3
geeks  for geeks
    g f g
    g f h l
Output:
geeksforgeeks
gfg
"""
t=int(input())
for i in range(1,t+1):
    str=input()
    p=str.strip()
    #print(p)
    s=p.replace(" ","")
    print(s)