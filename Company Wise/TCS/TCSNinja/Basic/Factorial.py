# Method 1
import math
num=int(input())
print(math.factorial(num))
# method 2
num=int(input())
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)