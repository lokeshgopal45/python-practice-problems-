num = int(input("Enter Input >3 and <7 for better pattern \n"))
print("Normal D")

# 1 Way Simple dots
for j in range(num + 1):
    if j == 0 or j == num:                      # In D letter we can see only First and last row having Lines
        print(num * "* ", end="\n")
    else:
        print("* " + (num - 2) * "  " + " *")  # In First and last Col we have *,except we have Spaces


# 2 way with curve
print("Curve D")
for j in range(num + 1):
    if j == 0 or j == num:                      # In D letter we can see only First and last row having Lines
        print((num-1) * "* ", end="\n")         # For some curve we have to print "-1" star
    else:
        print("* " + (num - 2) * "  " + " *")  # In First and last Col we have *,except we have Spaces
