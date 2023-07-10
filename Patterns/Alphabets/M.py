import math

num = int(input("Enter A Number \nEnter 5-7 "))
m = 2
for i in range(1, num + 1):
    if i > math.ceil(num / 2):
        print("* " + (num - 2) * "  " + "* ")
    elif i < math.ceil(num / 2):
        print(i * "* " + (num - m) * "  " + i * "* ")
        m += 2
    else:
        if num % 2 != 0:
            print("* " + math.floor(num / 2) * " " + "*" + math.floor(num / 2) * " " + " *")
        else:
            print("* " + math.floor(num / 2) * " " + "*" + math.ceil(num / 2) * " " + " *")
