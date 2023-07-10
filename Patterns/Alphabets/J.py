import math
num = int(input("Enter a ODD Number <=7 For Better Pattern \n"))
for i in range(num + 1):
    if i == 0:
        print(num * "* ")                               # In J letter we have Only First,last row(1/2)
    elif i == num:
        print(math.ceil(num / 2) * "* ")                # For last row we have to print 1/2 num *'s
    else:
        print((num - 1) * " " + "*")                    # For Middle line Character space
