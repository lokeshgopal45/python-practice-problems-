num=int(input())
sum=0
for i in str(num):
    sum+=(int(i)**len(str(num)))
print(sum) if sum==num else print("No")