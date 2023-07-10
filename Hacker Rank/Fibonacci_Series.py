#Fibonacci Series
a,b=0,1
n=15
count=0
if count<=n:
    for i in range(1,n):
        #if a%2==0:
        print(a,end=" ")
        c=a+b
        a=b
        b=c
    count+=1
