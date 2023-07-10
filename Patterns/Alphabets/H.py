num = int(input("Enter a Number >3 and <7 for better pattern \n"))
for i in range(num + 1):
    if i == num // 2:                                               # In H letter we have only middle Row,except spaces
        print(num * "* ")
    else:
        print("* " + (num - 2) * "  " + "* ")                       # For only First,last col we have * and spaces
