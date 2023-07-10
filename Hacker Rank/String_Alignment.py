# 6767 8403 2375 2325 6767 2352
testcase = int(input())
amount = 0
for i in range(testcase):
    car, date = map(int, input().split(" "))
    cars = list(map(int, input().split(" ")))
    if date % 2 == 0:
        count2 = []
        for i in cars:
            if i % 2 != 0:
                if cars.count(i) == 1:
                    amount += 100
                else:
                    count2.append(i)
        #print(amount)
        if len(count2) != 0:
            s = len(count2) - 1
            amount += ((s * 200) + 100)
            print(amount)
        else:
            print(amount)
    else:
        count2 = []
        for i in cars:
            if i % 2 == 0:
                if cars.count(i) == 1:
                    amount += 100
                else:
                    count2.append(i)
        #print(amount)
        if len(count2) != 0:
            s = len(count2) - 1
            amount += ((s * 200) + 100)
            print(amount)
        else:
            print(amount)

