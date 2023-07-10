num = int(input("Enter a Number \n"))
for i in range(num):
    if i == num - 1:
        print(" " + (num - 2) * " *" + " ")         # U having last Row *'s,remaining spaces
    else:
        print("*" + (num - 2) * "  " + " *")        # we have to print *'s at first & last column and spaces
