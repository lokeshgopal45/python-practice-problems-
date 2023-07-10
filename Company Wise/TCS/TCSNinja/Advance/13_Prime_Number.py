import time

st = time.time()
num = int(input())
count = 0
for i in range(2, num + 1):
    if num % i != 0:
        count += 1
print('PRIME') if (count + 2) == num else print('NOT PRIME')
lt = time.time()
print(str(format(lt - st, '.2f')) + "sec")
