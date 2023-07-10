"""
SPY NUMBER
A Number is said to be Spy Number product of the digits is equal to the sum of digits
Eg:
123
1+2+3==6==1*2*3

"""
Num = int(input())
N = str(Num)
pro = 1
sum = 0
for i in N:
    pro *= int(i)
    sum += int(i)
print("Spy Number") if pro == sum else print("Not a Spy Number")


