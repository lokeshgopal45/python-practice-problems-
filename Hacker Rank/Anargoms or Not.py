# *************Solved*****************
"""Given two strings s1 and s2, check if both the strings are anagrams of each other.
anagrams are have same letters in each word
Input : s1 = "listen"
        s2 = "silent"
Output : The strings are anagrams.

Input : s1 = "dad"
        s2 = "bad"
Output : The strings aren't anagrams.
"""

# s1 = "listen"  # input
# s2 = "silent"  # input
s1, s2 = input().split(" ")

p = sorted(s1)  # Sort the string
q = sorted(s2)  # Sort the string
if p == q:  # If Both are Equal
    print("Anagrams")  # They are Anagrams
else:  # Else
    print("Not anagrams")  # Not anagrams

""""# 1 Way
def anagrams(s1,s2):
    count1,count2=0,0
    for i in s1:                    # Checkig the ascii value of the string
        count1=count1+ord(i)        # Store it in Count1
    for i in s2:                    # Checkig the ascii value of the string
        count2 = count2 + ord(i)    # Store it in Count2
    if count1==count2 and (len(s1)==len(s2)):
        return "Yes"
    return "No"
s1,s2=input().split(" ")

print(anagrams(s1,s2))
"""
