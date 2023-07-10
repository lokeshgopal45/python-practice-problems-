bin=input()
sum=0
bin=bin[::-1]
for i in range(len(bin)):
    sum+=((2**i)*int(bin[i]))
print(sum)