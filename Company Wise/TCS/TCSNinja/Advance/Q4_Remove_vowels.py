"""
Remove Vowels
Given a String Str,Write a program to eliminate all vowels from it
Input:
abcdefghijklmnopqrstuvwxyz
Output:
bcdfghjklmnpqrstvwxyz

"""


def remove_vowels(l):
    check = "aeiouAEIOU"
    for i in l:
        if i in check:
            l.remove(i)
    return "".join(l)


str = "mTdxSkXRxqUziCXqNzUBPntZGtfRJDvJKryQAzycbEQFtJqWyuSi"
l = list(str)
print(remove_vowels(l))
