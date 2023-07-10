string = input()
str= "aeiouaAEIOU"
"""
# Method 1
ans=""
for i in string:
    if i not in str:
        ans+=i
print(ans)
"""
"""
# Method 2
string = string.lower()
for i in string:
    if not (i == "a" or i == "e" or i == "o" or i == "i" or i == "u"):
        print(i, end="")

"""
