num = int(input("Enter Input >3 and <7 for better pattern \n"))
for j in range(num + 1):
    if j == 0 or j==num//2:                          # In E letter same as B, but we don't have last column
        print(num * "* ")
    else:
        print("*")                                  # We don't have last column so we only print 1st column
