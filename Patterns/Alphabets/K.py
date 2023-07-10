import math
num=int(input("Enter a Number \n"))
for i in range(num+1):
    if i==num//2:                                   # In Letter K we have only Middle Row,all are spaces
        print(math.ceil(num/2)*"* ")
    else:
        print("*"+(num-1)*" "+"*")                  # For first,last column print *,remaining all are spaces

