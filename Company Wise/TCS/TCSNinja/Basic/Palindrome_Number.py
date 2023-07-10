num = int(input())
"""
    rev = ""
    while num != 0:
        rem = num % 10
        rev += str(rem)
        num = num // 10
"""
N=str(num)
if int(N[::-1])== num:
    print("Yes")
else:
    print("No")
