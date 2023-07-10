num = int(input("Enter a Number \n"))
for i in range(num):
    if i == 0 or i == num - 1 or i == num // 2:      # S having first,middle and last rows *'s
        print(num * " *")
    elif i > num // 2:
        print("  " + (num - 2) * "  " + " *")        # This is After middle Row we want only *on last column and spaces
    else:
        print(" *")                                  # This is for Before Middle Row only we want * and spaces
