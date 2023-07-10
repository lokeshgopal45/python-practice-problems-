"""
Find the first repeated word in a string in Python using Dictionary Given a string,
Find the 1 st repeated word in a string.

Examples:
Input: "Ravi had been saying that he had been there"
Output: had

Input: "Ravi had been saying that"
Output: No Repetition

Input: "he had had he"
Output: he
"""
string="he had had he"
target="he"
temp=list(string.split(" "))
ans=[]
for i in temp:
    if temp.count(i)>1:
        ans.append(i)
if target in temp:
    print(max(ans))
else:
    print("No Repetition")