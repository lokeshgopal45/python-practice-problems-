ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
for i in range(0,len(ar),2):

ar.sort()
print(ar)
count = 0
for i in range(0, len(ar)):
    if ar[i] == ar[i + 2]:
        count += 1
# print(count)
