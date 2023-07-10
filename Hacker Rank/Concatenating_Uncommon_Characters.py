"""
Concatenated string with uncommon characters in Python
Two strings are given and you have to modify 1st string such that
all the common characters of the 2nd strings have to be removed and
the uncommon characters of the 2nd string have to be concatenated with uncommon characters of the 1st string.
Examples:
Input : S1 = "aacdb" ,S2 = "gafd"
Output : "cbgf"
Input : S1 = "abcs" ,S2 = "cxzca";
Output : "bsxz"
"""
x,y="abcs","cxzca"
Z=x+y
#print(Z)
Ans=[]
for i in Z:
    if not(Z.count(i)>1):
        Ans.append(i)
print(*Ans,sep="")