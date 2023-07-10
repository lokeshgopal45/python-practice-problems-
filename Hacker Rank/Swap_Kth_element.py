"""
testcase=int(input())
for i in range(testcase):
    N,K=map(int,input().split(" "))
    li=list(map(int,input().split(" ")))
    li[-K],li[K-1]=li[K-1],li[-K]
    print(*li)
"""
testcase=int(input())
for i in range(testcase):
    N=int(input())
    Li=list(map(int,input().split(" ")))
    print(Li[::-1])