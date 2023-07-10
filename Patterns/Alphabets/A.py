num = int(input("Enter A Number\n"))
for j in range(num + 1):
    if j == 0 or j == num//2:                     # In A letter we can see only First row and middle row having Lines
        print(num * "* ", end="\n")
    else:
        print("*" + (num - 2) * "  " + " *")       # In First Col and Last col we have *,except we have Spaces

# Note:
# Num-2 means that number of characters space we have to give if we give "num" spaces , pattern may  be wrong
