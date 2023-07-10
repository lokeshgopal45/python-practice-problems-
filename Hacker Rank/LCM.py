num1, num2 = map(int, input().split(" "))
arr1 = []
arr2 = []
HCF = 1
for i in range(1, num2):
    if num2 % i == 0:
        arr1.append(i)
for j in range(1, num1):
    if num1 % j == 0:
        arr2.append(j)
for i in arr1:
    if i in arr2:
        HCF *= i
print(HCF)
