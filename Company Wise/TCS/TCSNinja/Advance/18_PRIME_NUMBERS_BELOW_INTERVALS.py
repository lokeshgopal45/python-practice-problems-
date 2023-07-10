def prime(num1, num2):
    for i in range(num1, num2):
        count = 0
        for j in range(2, i + 1):
            if i % j != 0:
                count += 1
        if (count + 2) == i:
            print(i, end=" ")


prime(1, 1000)
