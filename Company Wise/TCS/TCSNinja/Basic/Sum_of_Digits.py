# Method 1
num=int(input())
N=str(num)
sum=0
for i in N:
    sum+=int(i)
print(sum)
# Method 2
num=int(input())
sum=0
while num!=0:
    rem=num%10
    sum+=rem
    num=num//10
print(sum)