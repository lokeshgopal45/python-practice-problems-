num = int(input("Enter a Number \n"))
for i in range(num + 1):
    if i == 0 or i == num:                          # In Letter "O" we have first,last Row
        print(num * "* ")
    else:
        print("* " + (num - 2) * "  " + "*")        # and First,last columns
