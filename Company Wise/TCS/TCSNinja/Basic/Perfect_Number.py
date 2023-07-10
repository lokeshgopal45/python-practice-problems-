# If a Number is said to be perfect number if sum of factors is equal to the given number
num=int(input())
sum=0
for i in range(1,num-1):
    if num%i==0:
        sum+=i
print("Yes") if sum==num else print("No")