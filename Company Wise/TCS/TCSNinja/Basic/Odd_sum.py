lower,upper=map(int,input().split(" "))
sum=0
for i in range(lower,upper):
    if i%2!=0:
        sum+=i
print(sum)