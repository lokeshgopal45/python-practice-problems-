
import time

st = time.time()


def prime_in_range(num):
    for i in range(2, num + 1):
        count = 0
        for j in range(2, i + 1):
            if i % j != 0:
                count += 1
        if (count + 2) == i:
            print(i, end=" ")


prime_in_range(100.
               )
lt = time.time()
print()
print(str(format((lt - st), '.2f')) + "sec")


