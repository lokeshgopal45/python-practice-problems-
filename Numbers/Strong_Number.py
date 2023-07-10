"""
Strong Number:
A Number is said to be Strong Number if the Sum of Individual factors is equal to Given Number
Eg:
Number:145
1! ---> 1
4! ---> 24
5! ---> 120
Sum --> 145
so here sum is equal to number so it is Strong number And it is also Called Krishna Murthy Number
"""
Number=int(input())
N = str(Number)
sum = 0
for i in N:
    fact = 1
    for j in range(1, int(i) + 1):
        fact *= j
    sum += fact
print("Strong Number ") if Number == sum else print("NOT A Strong Number ")

