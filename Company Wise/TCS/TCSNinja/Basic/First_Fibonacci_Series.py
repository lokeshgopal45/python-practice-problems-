n1,n2=0,1
count=0
num=int(input())
while count<num:
    print(n1,end=" ")
    n3=n1+n2
    n2=n1
    n1=n3
    count+=1
