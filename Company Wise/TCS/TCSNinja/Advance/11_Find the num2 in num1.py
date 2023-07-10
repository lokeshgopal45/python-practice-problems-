num1,num2=map(int,input().split(" "))
count=0
for i in str(num1):
    if int(i)==num2:
        count+=1
print(count)