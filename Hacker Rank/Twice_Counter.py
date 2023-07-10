"""
Given Array of n words.
Some words are repeated twice we need count of that words
Input:                                                  Output:
hate love peace love peace hate love peace love peace       1
Tom Jerry Thomas Tom Jerry Courage Tom Courage
"""
testcase=int(input())
for i in range(testcase):
    N=int(input())
    li=input().split(" ")
    count=0
    list=[]
    for i in li:
        if li.count(i)==2:
            list.append(i)
    print(len(set(list)))