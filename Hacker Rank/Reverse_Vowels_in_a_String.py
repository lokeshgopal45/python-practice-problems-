"""
Given a string, reverse only the vowels present in it and print the resulting string.
Input: First line of the input file contains an integer T denoting the number of test cases.
Then T test cases follow. Each test case has a single line containing a string.

Output: Corresponding to each test case, output the string with vowels reversed.

Example:
Input:
4
geeksforgeeks
practice
wannacry
ransomware

Output:
geeksforgeeks
prectica
wannacry
rensamwora
"""
s="aeiouAEIOU"
t=int(input())
ans=[]
Ans=[]
for i in range(1,t+1):
    str="geeksforgeeks"
    for i in str:
        if i in s:
            ans.append(i)
    p=ans[::-1]
    l=len(p)
    j=0
    for i in str:
        if i not in s:
            Ans.append(i)
        else:
            P=p[j]
            Ans.append(P)
            j+=1
    print(*Ans,sep="")