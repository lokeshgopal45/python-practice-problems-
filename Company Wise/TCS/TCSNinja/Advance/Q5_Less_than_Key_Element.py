"""
Q5. Less than Key element
Print and count all the numbers which are less than a given key element from a given array
Input Format:
Input contains the no of elements , key value and the elements
Output Format:
print the count
"""
count = 0
m, n = map(int, input().split(" "))
s = list(map(int, input().split(" ")))
for i in s:
    if i < n:
        count += 1

print(count)
