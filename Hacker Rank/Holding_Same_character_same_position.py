"""
Given two string of equal length i.e s1 and s2, you need to find how many time the corresponding position in two strings hold exactly the same characters
and if a string contains any uppercase character convert that into lowercase and then find the count.

Input:
The First line of the input contains an integer T denoting the number of test cases. For each test case, there are two strings input s1 and s2 of equal length.
Output:
For each test case, the output is an integer value displaying the number of times characters are same at the corresponding position.
Constraints:
1<=T<=100
The string should contain only alphabets.

Example:
Input:
3
choice chancE
geek Gang
life Tech

Output:
4
1
0
"""
T=int(input())
count=0
for i in range(1,T+1):
    N1,N2=input().split(" ")
    if len(N1)==len(N2):
        for i in range(len(N1)):
            if N1[i].lower()==N2[i].lower():
                count+=1
    print(count)