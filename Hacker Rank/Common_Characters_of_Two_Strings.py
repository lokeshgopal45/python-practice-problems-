"""
Python code to print common characters of two Strings in alphabetical order
Given two strings, print all the common characters in lexicographical order. If there are no common letters, print -1. All letters are lower case.

Examples:

Input :
string1 : geeks string2 : forgeeks
Output : eegks
Explanation: The letters that are common between
the two strings are e(2 times), k(1 time) and
s(1 time).
Hence the lexicographical output is "eegks"

Input :
string1 : hhhhhello string2 : gfghhmh
Output : hhh

"""
string1="hhhhhello"
string2="gfghhmh"
S=[]
for i in string1:
    if i in string2:
        S.append(i)
print(*sorted(S),sep="")