num = int(input("Enter a Number \n"))
for i in range(num):
    if i == 0:
        print(num * "* ")                           # T is having Only First row *,and remaining spaces
    else:
        print((num - 2) * " " + " *")               # it is having Middle Column so we have num-2 character space
# Note
# num-2 is character space
print("""
For even Number character space is some what looks different but it is possible !! lets give some Even Input also
    """)
