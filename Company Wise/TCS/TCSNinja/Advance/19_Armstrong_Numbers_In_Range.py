import time

st = time.time()


def armstrong(number1, number2):
    arm = []
    for i in range(number1, number2 + 1):
        Nu = str(i)
        count = 0
        for j in Nu:
            count += (int(j) ** len(Nu))
        if count == i:
            arm.append(i)
    if len(arm) != 0:
        print(*arm)
    else:
        print("No elements")


armstrong(1, 100000)
lt = time.time()
print(format((lt - st), '.2f') + "sec")
