Mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
"""
# Method 1
TransPose = []
for i in range(0, len(Mat) - 1):
    temp = []
    for j in range(0, len(Mat)):
        temp.append(Mat[j][i])
    TransPose.append(temp)
print(TransPose)

"""
"""
# Method 2:
for i in range(0, len(Mat)):
    for j in range(len(Mat)):
        print(Mat[j][i], end=" ")
        if j == len(Mat)-1:
            print()

"""
