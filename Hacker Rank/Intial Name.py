"""
Print the initials of a name with last name in full
Given a name, print the initials of a name(uppercase) with last name(with first alphabet in uppercase) written in full separated by dots.
Examples:

Input : geeks for geeks
Output : G.F.Geeks

Input : mohandas karamchand gandhi
Output : M.K.Gandhi
"""
s1="Jehangir Ratanji Dadabhoy Tata"
"""
list=s1.split()
Full_name=""
if len(list)>=3:
    first=list[0][0]
    second=list[1][0]
    last_name=list[-1]
    name = first.upper() + "." + second.upper() + "." + last_name.capitalize()
    print(name)
else:
    for i in range(len(list)-1):
        fake=list[i]
        first=fake[0].upper()
    last=list[-1].capitalize()
    name=first+"."+last
    print(name)
""" # 1 Way
"""
name=[]
temp=list(s1.split())
#print(temp)
for i in range(len(temp)-1):
    fake=temp[i]
    name.append(fake[0].upper())
name.append(temp[-1].capitalize())
print(*name,sep=".")
""" # 2 Way
