a, b = map(int, input().split(" "))
print(bin((a + b)).replace("0b", ""))
num=int(input())
for i in str(num):
    print(bin(int(i)).replace("0b", ""))