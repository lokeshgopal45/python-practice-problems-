"""
Row, col = map(int, input().split(" "))
val=int(input())
k = 1
Mat = []
for i in range(1,Row+1):
    mat = []
    for j in range(k, (i * col)+1):
        mat.append(j)
    Mat.append(mat)
    k += Row

"""
w = [[12, 3], [4, 5]]
val=3
for i in w:
    for j in w:
        print(i,j)
