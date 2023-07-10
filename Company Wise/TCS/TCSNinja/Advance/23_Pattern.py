n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        print(str(i)*(n-1)+str(i+1))
    else:
        print(str(i) * (n - 1) + str(i + 1))
