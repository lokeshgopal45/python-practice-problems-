num = int(input("Enter Input >3 and <7 for better pattern \n"))
print("Normal G")
for j in range(num + 1):
    if j == 0 or j == num // 2 or j == num:        # In G letter same as B,we have first,last and middle column
        print(num * "* ")
    elif j>=(num//2)+1:                            # In G letter we have first and last column after middle Row
        print("*" + (num - 2) * "  " + " *")
    else:
        print("*")                                 # In G letter we don't have last column below middle row

print("Curve G")
# 2 way
for j in range(num + 1):
    if j == 0 or j == num // 2 or j == num:
        print((num-1) * "* ")
    elif j>(num//2):
        print("*" + (num - 2) * "  " + " *")
    else:
        print("*")
