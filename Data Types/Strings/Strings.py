str = "My Name is jessa"
s1 = str.split(" ")
ans = []
for i in s1:
    ans.append(i[::-1])
print(" ".join(ans))