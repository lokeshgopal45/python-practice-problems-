# Method 1
num = int(input())
N = str(num)
print(N[::-1])
# Method 2
num = int(input())
rev=""
while num!=0:
    rem=num%10
    rev+=str(rem)
    num=num//10
print(rev)