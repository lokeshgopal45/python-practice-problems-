"""
Check if both halves of the string have same set of characters in Python
Given a string of lowercase characters only, the task is to check if it is possible to split a string from middle which will gives two halves having the same characters and same frequency of each character.
If the length of the given string is ODD then ignore the middle element and check for the rest.

Examples:

Input : abbaab
Output : NO

The two halves contain the same characters but their frequencies do not match so they are NOT CORRECT

Input : abccab
Output : YES
"""
s1 = "abcdfgabcd"
first_count = 0
second_count = 0
length = len(s1)
if length % 2 == 0:
    first = s1[:int(length / 2)]
    second = s1[int(length / 2) + 1:]
    for i in first:
        first_count += ord(i)
    for i in second:
        second_count += ord(i)
else:
    first = s1[:int(length // 2)]
    second = s1[int(length // 2):]
if first_count == second_count:
    print("yes")
else:
    print("No")
