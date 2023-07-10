n = int(input())
for i in range(n + 1):
    for j in range(i, i + 1):
        print(str(j) * j, end="\n")
