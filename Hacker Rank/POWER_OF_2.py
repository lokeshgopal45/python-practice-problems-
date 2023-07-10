import time
st=time.time()
test=int(input())
for i in range(test):
    count = 0
    N=int(input())
    for j in range(60):             # Becoz 2*60 same as N constranit value 
        if 2**j==N:
            count+=1
    if count>0:
        print("YES")
    else:
        print("NO")

et=time.time()
print(et-st)