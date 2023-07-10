num=int(input())
count=0
for i in range(2,num):
    if num%i!=0:
        count+=1
if (count+2)==num:
    print(format(num**0.5,'.2f'))
else:
    print(format(0,'.2f'))