"""
number=int(input())
# Method 1
for i in range(number):
    for j in range(number - i):
        print(end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
# Method 2 May or May not be
for i in range(number + 1):
    for j in range(number + 1, 0, -1):
        if j > i:
            print(" ", end="")
        else:
            print("*", end=" ")
    print()

"""
# Method 2 May or May not be
number = 5
for i in range(number + 1):
    for j in range(number - i):
        print(end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
