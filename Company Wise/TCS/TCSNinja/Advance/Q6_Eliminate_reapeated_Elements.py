"""
Q6. Eliminate Repeated Elements
Given two positive integer arrays ary1 and arr2 of lengths len1 and len2 respectively. write a program to count the number of
elements which are not common In the arrays.
The input to the function distinctElementCount of two arrays arr1 and arr2 and their lengths len1 and len2 respectively.
The function return the number of elements which are not common in both arrays.
Example:
arr1 = {1, 2,3, 4, 5, 6, 7, 8, 9, 10}, lent = 10
arr2 = {11, 12, 13, 4, 5, 6, 7, 18, 19, 20}, len2 = 10
The distinct elements are 1, 2, 3, 8, 9, 10, 11, 12, 13, 18, 19 and 20 so the function should return 12.
Input Format:
Input contains the length of the arrays and the values
Output Format:
Print non repeating elements in {} and the count
"""
"""
arr1 = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [11, 12, 13, 4, 5, 6, 7, 18, 19, 20]
arr3=arr1+arr2
count=0
for i in arr3:
    if arr3.count(i)==1:
        count+=1
        print(i,end=" ")
print("length:",count)

""" # 1 Way
"""
def distinct_ELement_count(arr1, arr2):
    arr3 = arr1 + arr2
    count = 0
    for i in arr3:
        if arr3.count(i) == 1:
            count += 1
            # print(i, end=" ")
    return count


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [11, 12, 13, 4, 5, 6, 7, 18, 19, 20]
print(distinct_ELement_count(arr1, arr2))

""" # 2 Way
