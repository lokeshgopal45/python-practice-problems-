"""
You are given an array of elements and a number your task is to print the first half in ascending order and second half
in descending order
Eg:
arr=[6, 10, 5, 4, 9, 120, 4, 6, 10],n=4



"""
nums = [6, 3,10, 5, 4, 9, 120, 4, 6, 10]
n=4
nums.sort()
s=sorted(nums,reverse=True)
print(nums[:n-1]+s[:n-1])
