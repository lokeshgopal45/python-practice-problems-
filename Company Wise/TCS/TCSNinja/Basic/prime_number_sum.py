lower,upper=map(int,input().split(" "))
sum=0
for i in range(lower,upper):
    count = 0
    for j in range(2,i):
        if i%j!=0:
            count+=1
    if (count+2)==i:
        sum+=i
        #print(i,end=" ")
print(sum)