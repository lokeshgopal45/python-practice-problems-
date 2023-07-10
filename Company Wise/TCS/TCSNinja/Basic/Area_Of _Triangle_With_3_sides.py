s1,s2,s3=map(float,input().split(" "))
s=(s1+s2+s3)/2
print(format(((s*(s-s1)*(s-s2)*(s-s3))**0.5),'.2f'))