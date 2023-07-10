"""

def rev(num):
    ans = ""
    while num != 0:
        rev = num % 10
        ans += str(rev)
        num = num // 10
    return ans


num = -10200
N = str(num)
if N.startswith("-"):
    num = N[1:]
    p = rev(int(num))
    count = 0
    if p.count("0") > 0:
        for i in p:
            if i == "0":
                count += 1
            else:
                break
        print("-" + p[count:])
    else:
        print("-" + p)
else:
    p = rev(num)
    count = 0
    if p.count("0") > 0:
        for i in p:
            if i == "0":
                count += 1
            else:
                break
        print(p[count:])
    print(p)

"""
"""
def reverse(x):
    N = str(x)
    if N.startswith("-"):
        num = int(N[1:])
        ans = ""
        while num != 0:
            rev = num % 10
            ans += str(rev)
            num = num // 10
        count = 0
        if ans.count("0") > 0:
            for i in ans:
                if i == "0":
                    count += 1
                else:
                    break
            return "-"+ans[count:]
        else:
            return "-"+ans
    else:
        num = int(N)
        ans = ""
        while num != 0:
            rev = num % 10
            ans += str(rev)
            num = num // 10
        count = 0
        if ans.count("0") > 0:
            for i in ans:
                if i == "0":
                    count += 1
                else:
                    break
            return ans[count:]
        else:
            return ans
num=[1234,-336,-120002,-5555]
for i in num:
    print(reverse(i))
"""
