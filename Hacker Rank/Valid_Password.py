"""
In this program, we will be taking a password as a combination of alphanumeric characters along with special characters,
and check whether the password is valid or not with the help of few conditions.
Primary conditions for password validation :

Minimum 8 characters.
The alphabets must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ].

Examples:
Input : R@m@_f0rtu9e$    Input : Rama#fortu9e
Output : Valid Password  Output : Invalid Password

"""
password="Rama#fortu9e"
a,b,c,d,e=0,0,0,0,0
for i in password:
    if i.islower():
        a+=1
    elif i.isupper():
        b+=1
    elif i.isdigit():
        c+=1
    elif i=="_" or "@" or"$":
        d+=1
if a>=1 and b>=1 and c>=1 and d>=1 and (a+b+c+d)==8:
    print("Valid")
else:
    print("Invalid")