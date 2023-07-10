"""
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
"""
import time
st=time.time()
array=[2,7,11,15]
target=9
list=[]
for i in range(len(array)):
    first=array[i]
    for j in range(len(array)):
        second=array[j]
        if first+second==target and first!=second:
            print(array.index(first),array.index(second))
            break
lt=time.time()
print(lt-st)
"""
"""
s="123,456,789.00"
Li=list(s.split(","))
print(Li)
print(list(s))
Q=s.replace(",",".")
print(Q)
"""
a = [2, 7, 9, 11]
target = 9
ans = []
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if (a[i] == target - a[j]):
            ans.append(i)
            ans.append(j)

print(*ans)
