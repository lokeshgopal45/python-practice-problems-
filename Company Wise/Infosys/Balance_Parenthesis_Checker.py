string = "(([))(){{{}}}[]]]"
a = string.count('(')
b = string.count('[')
c = string.count('{')
ans=""
for i in string:
    count = 0
    if string.count('(') == string.count(')'):
        count += 1
    elif string.count('[') == string.count(']'):
        count += 1
    elif string.count('{') == string.count('}'):
        count += 1
if count == 3:
    print(True)
else:
    print(False)
