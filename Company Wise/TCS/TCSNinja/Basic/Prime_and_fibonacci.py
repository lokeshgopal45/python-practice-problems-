limit = 30
number = int(input("Enter "))
series = []
n1, n2 = 0, 1
count = 0
fib = 1
prime = 2
while count < limit:
    series.insert(fib, n1)
    n3 = n1 + n2
    n2 = n1
    n1 = n3
    count += 1
    fib += 2
for i in range(1, limit + 1):
    # Prime
    count = 0
    for j in range(2, i):
        if i % j != 0:
            count += 1
    if (count + 2) == i:
        series.insert(prime, i)
        prime += 2
        # print(i)
series = series[1:]
print(*series)
print(series[number - 1])
