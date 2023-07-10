Number = int(input())
N = str(Number)
arr1 = []
while N=!1:
    SUM = 0
    for i in N:
        SUM += (int(i) ** 2)
    print(SUM)
    arr1.append(SUM)
    N = str(SUM)
    if N == "1":
        break
    else:
        N=str(Number)

if arr1[-1] == 1:
    print("Happy Number ")
else:
    print("Not Happy Number")
