array_size,sort=map(int,input().split(" "))
array=list(map(int,input().split(" ")))
array.sort()
rev=array[::-1]
print(*array[:sort]+rev[:(array_size-sort)])