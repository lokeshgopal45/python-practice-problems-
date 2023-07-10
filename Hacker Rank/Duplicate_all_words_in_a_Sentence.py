"""
Remove all duplicates words from a given sentence
Given a sentence containing n words/strings. Remove all duplicates words/strings which are similar to each others.

Examples:
Input : Geeks for Geeks
Output : Geeks for

Input : Python is great and Java is also great
Output : is also Java Python and great

"""
string="Python is great and Java is also great"
temp=list(string.split(" "))
ans=[]
final_ans=[]
for i in temp:
    if (string.count(i)==1) or ((string.count(i)>1)and (i not in ans)):
        ans.append(i)
print(*ans)