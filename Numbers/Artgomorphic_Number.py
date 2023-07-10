"""
ARTHOMORHIC NUMBER:
A Number is said to be arthomorphic number if last digit of its  Square Number is Equal to Given Number
Eg:
1)5 ---> 25
          5 --->5
2)6 ---> 36
          6 --->6
"""
Number = int(input())
Sqaure = Number ** 2
Ans = str(Sqaure)
print("arthomorphic Number ") if Ans[-1] == str(Number) else print("NOT a arthomorphic ")
