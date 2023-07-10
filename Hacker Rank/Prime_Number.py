"""
N=int(input())
count=0
for n in range(2,N+1):
    for i in range(2,n+1):
        if n%i!=0:
            count+=1
    if (count+2)==n:
        print(n)
"""
