num = int(input())
arr = list(map(int, input().split(" ")))
arr1=[]
for i in range(0, len(arr), 2):
    arr1.append(arr[i])
arr1.sort()
print(*arr1)