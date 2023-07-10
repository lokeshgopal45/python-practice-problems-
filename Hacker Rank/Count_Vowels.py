"""
For a Given Input You are going to Count No of Vowels
Eg:
Input:"Geeks For Geeks"
Output:
"""
# 1 Way
import time
st=time.time()
Input="Geeks For Geeks"
vow=["a","e","i","o","u"]
count=0
list=[]
for i in Input:
    if i in vow :#and i not in list
        list.append(i)
        count+=1
print(count)
print(*list)
lt=time.time()
print("Time :{} Sec".format(lt-st))
# 1 way
"""
def checking_Vow(word,letters):
    output=[i for i in word if i in letters]
    return output

word="Geeks For geeks"
letters="AEIOUaeiou"
print(checking_Vow(word,letters))
"""