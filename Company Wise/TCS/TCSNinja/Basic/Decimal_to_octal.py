num=input()
num=num[::-1]
sum=0
for i in range(len(num)):
    sum+=((8**i)*int(num[i]))
print(sum)