nums = [6, 10, 5, 4, 9,6]
"""
# Method 1
r = set(nums)
print(len(list(r)))
"""
#nums = [1, 1, 2]
# Method 2


ans = []
for i in nums:
    if i not in ans:
        ans.append(i)
print(ans)

# """
