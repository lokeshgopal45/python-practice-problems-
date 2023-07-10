"""
Given a string ,reverse only the vowels present in it print the resulting string
Input:                  Output:
GeeksforGeeks           GeeksforGeeks
practice                prectica
wannacry                wannacry
ransomewhere            rensamwora
"""
str = "aeiouAEIOU"
string=input()
for i in string:
    if i in str:
        print(True)
        break