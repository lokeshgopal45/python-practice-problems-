"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last
word (last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

"""
st=input()
str=st.split( )
print(str)
if str[-1]==1:
    print(0)
elif len(str)>1:
    for i in range(len(str)-1,0,-1):
        print(len(str[i]))
        break
else:
    print(len(str))