"""
Second most repeated word in a sequence in Python
Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.
(Considering no two words are the second most repeated, there will be always a single word).

Examples:
Input : {"aaa", "bbb", "ccc", "bbb",
         "aaa", "aaa"}
Output : bbb

Input : {"geeks", "for", "geeks", "for",
          "geeks", "aaa"}
Output : for
"""

string="'aaa' 'bbb' 'ccc' 'bbb' 'aaa' 'aaa'"
temp=list(string)
ans=[]
print(temp)
for i in temp:
    if temp.count(i)>1:
        print(i)