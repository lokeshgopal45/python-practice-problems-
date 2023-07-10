"""
Given two strings, check if s1 is there in s2.
1
Input : s1 = geeks s2=geeks for geeks
Output : yes
2
Input : s1 = geek s2=geeks for geeks
Output : yes
"""
"""
s1="India "                  # Sub String
s2="India is My Country"    # String
if s1.find(s2):             # Find Sub String is in String
    print("YES")            # If it is Found print("YES")
else:
    print("NO")             # else "NO"
""" # 1 Way
"""
s1="My"
s2="India is My Country"
list=s2.split(" ")
count=0
for i in list:
    if i==s1:
        count+=1
        break
    else:
        count=0
if count>=1:
    print("yes")
else:
    print("No")
""" # 2 Way
"""
s1=" "
s2='India is  My country'
if s2.count(s1)>0:
    print("yes")
else:
    print("NO")
""" # 3 Way
