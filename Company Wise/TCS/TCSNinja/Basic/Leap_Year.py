#def leap(year):
year=int(input())
if year%4==0:
    if year%100:
        print("yes")
    elif year%400==0:
        print("yes")
    else:
        print("No")
else:
    print("No")
#s=[i for i in range(1000,1700)]
#for i in s:
#    leap(i)