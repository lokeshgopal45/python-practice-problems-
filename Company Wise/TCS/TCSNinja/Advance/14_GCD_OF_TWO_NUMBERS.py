# Method 1 Some what time complexity
"""
import time
st=time.time()
num1, num2 = map(int, input().split(" "))
GCD=[]
if num1 > num2:
    largest = num1
else:
    largest = num2
for i in range(1, largest):
    if num1 % i == 0 and num2 % i == 0:
        GCD.append(i)
print(GCD[-1])
lt=time.time()
print(str(format((lt-st),'.2f'))+"sec")
"""
# Method 2 less time complexity
"""
import time
st=time.time()
factors1=[]
factors2=[]
HCF=[]
num1, num2 = map(int, input().split(" "))
for i in range(1,num1):
    if num1%i==0:
        factors1.append(i)
for i in range(1,num2):
    if num2%i==0:
        factors2.append(i)
for i in factors1:
    if i in factors2:
        HCF.append(i)
print(max(HCF))
lt=time.time()
print(str(format((lt-st),'.2f'))+"sec")

"""
