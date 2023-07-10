testcase=int(input())
for i in range(testcase):
    N=int(input())
    s=list(map(int,input().split(" ")))
    print(max(s),min(s))
