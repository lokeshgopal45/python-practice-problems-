test=int(input())
for i in range(test):
    N,D=map(int,input().split(" "))
    s=list(map(int,input().split(" ")))
    print(*(s[D:]+s[:D]))