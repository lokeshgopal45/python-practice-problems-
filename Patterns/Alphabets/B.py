num = int(input("Enter Number\n"))
for j in range(num + 1):
    if j == 0 or j == num // 2 or j == num:  # In B letter we can see Three Rows first,last and middle one
        print((num) * "* ", end="\n")
    else:
        print("*" + (num - 2) * "  " + " *")  # In First Col and Last col we have *,except we have Spaces

# Note:
# Num-2 means that number of characters space we have to give if we give "num" spaces , pattern may  be wrong
# B simply looks like "8" so for Eight also same code
