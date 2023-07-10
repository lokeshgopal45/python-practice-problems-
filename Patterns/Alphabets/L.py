num=int(input("Enter a Number \n"))
for i in range(num+1):
    if i==num:                          # In "L" Letter we have only last Row
        print(num*"* ")
    else:                               # and we have only First column
        print("*")