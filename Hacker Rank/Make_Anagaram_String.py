"""Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to
remove a character from any string. Find the minimum number of characters to be deleted to make both the strings
anagram. Two strings are called anagram of each other if one of them can be converted into another by rearranging its
letters.

Example 1:
Input: S1 = bcadeh S2 = hea
Output: 3
Explanation: We need to remove b, c and d from S1.

Example 2:
Input: S1 = cddgk S2 = gcd
Output: 2
Explanation: We need to remove d and k from S1.

Your Task:
Complete the function remAnagram() which takes two strings S1, S2 as input parameter,
and returns minimum characters needs to be deleted.

#def remAnagram():

str1="bcadeh"
str2="hea"
temp1 = list(str1)
temp2 = list(str2)
ans=[]
count=0
for i in temp2:
    j=i
    if j in temp1:
        temp2.remove(j)
    else:
        count+=1
        count+=len(temp2)
print(count)
""""""