"""
Perfect Number:
    Sum of their 'factors' is Equal to the Given Number then it is called Perfect Number
Eg:
1)
Num=6
Factors=1,2,3
sum of factors are 1+2+3==6


We have only 4 perfect Numbers <10,000 ie, 6,28,496 and 8128.
"""
number = int(input())
def perfect_number(number):
    flag = 0
    for i in range(1, number):
        if number % i == 0:
            flag += i
    if flag == number:
        return str(number) + " is PerfectNumber"
    return str(number) + " is Not PerfectNumber"

print(perfect_number(number))
