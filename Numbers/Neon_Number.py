"""
NEON NUMBER
A Neon number is said to be Neon Number if  sum of the digits in a square of a given Number is equal to Given Number
Eg:
9
9 ---> 81
        8+1 ---> 9
So 9 is Neon Number
"""
number = int(input())
Square = number ** 2
sum = 0
for i in str(Square):
    sum += int(i)
if sum == number:
    print("Neon Number")
else:
    print("Not a Neon Number")
