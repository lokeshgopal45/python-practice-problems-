"""
Given an array of 4 digits,return the largest 24 hour time,that can be made
The smallest 24 hour time is 00.00,largest time is 23.59.
Return the answer as a string length of 5.if no valid time can be made return empty string
Input :[1,2,3,4]        [5,5,5,5]
Output:"23:41"          ""
"""
from itertools import permutations
arr=[2,4,0,0]
count=0
for i in arr:
    if i>4:
        count+=1
if count!=len(arr):
    s=permutations(arr)
    for i in s:
        li=list(i)
        p="".join(str(li[:2]))
else:
    print('" "')

