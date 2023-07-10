test=int(input())
for i in range(test):
    N=int(input())
    s=list(map(int,input().split(" ")))
    K=int(input())
    s.sort()
    print(s[K-1])