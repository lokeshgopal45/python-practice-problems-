"""
Sort words of sentence in ascending order
Given a sentence, sort it alphabetically in ascending order.

Examples:
Input : to learn programming refer geeksforgeeks
Output : geeksforgeeks learn programming refer to

Input : geeks for geeks
Output : for geeks geeks
"""
"""
string="geeks for geeks"            # Input
temp=string.split(" ")              # Split the word
print(*sorted(temp))                # Sort the Entire String
""" # 1 Way