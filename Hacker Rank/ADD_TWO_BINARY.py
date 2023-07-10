a, b = input().split(" ")  # Input
First = (8 - len(a)) * "0" + a
Second = (8 - len(b)) * "0" + b
# print(bin(int(First,2)+int(Second,2)).replace("0b",""))
print(bin(int(a, 2) + int(b, 2)).replace("0b", ""))
# add two binary values and convert to int and represent in binary
