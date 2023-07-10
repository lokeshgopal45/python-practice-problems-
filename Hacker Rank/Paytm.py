"""
You are given an array and elements Each Element Represents the Forward length Your task is to find the minimum distance
Covered Element

"""
arr = [1, 4, 1, 5, 7, 2, 3, 6, 7, 0]
flag=0
for i in range(len(arr)):
    if (i + arr[i] )== len(arr) - 1:
        if arr[i] != 0:
            print(arr[i])