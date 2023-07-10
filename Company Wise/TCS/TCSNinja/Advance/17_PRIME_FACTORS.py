def is_prime(i):
    count = 0
    for j in range(2, i):
        if i % j != 0:
            count += 1
    if (count + 2) == i:
        print(i,end=" ")


def factors(num):
    if is_prime(num):
        print(num)
    for i in range(1, num):
        if num % i == 0:
            is_prime(i)


factors(14416)
