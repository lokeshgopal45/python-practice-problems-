num=int(input("Enter a Number \n"))
for i in range(num+1):
    if i==0 or i==num//2:
        print(num*"* ")
    elif i<num//2:
        print("*"+(num-2)*"  "+" *")
    else:
        print(" "+(num-2)*"  "+" *")