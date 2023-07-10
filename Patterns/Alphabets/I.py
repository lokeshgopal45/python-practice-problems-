num = int(input("Enter a ODD Number <=7 for Better Pattern \n"))
for i in range(num + 1):
    if i == 0 or i == num:                  # In I letter we have only First and last Row
        print(num * "* ")
    else:
        print((num - 2) * " " + " *")       # In I letter we have Middle Column so we have num-2 character space
# Note
# num-2 is character space
print("""
For even Number character space is some what looks different but it is possible !! lets give some Even Input also
    """)
