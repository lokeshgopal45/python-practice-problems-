num = int(input("Enter Input >3 and <7 for better pattern \n"))
for j in range(num + 1):
    if j == 0 or j == num:                     # In C letter we can see only First and last row having Lines
        print(num * "* ", end="\n")
    else:
        print("*")                             # In First Col we have *,except we have Spaces

