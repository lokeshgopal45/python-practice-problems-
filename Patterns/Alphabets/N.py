# N Alphabet Needs work
num=int(input("Enter a Number"))
j=1
k=0
for i in range(1,num+1):
    if i==1 or i==num:
        print("* "+(num-2)*" "+"* ")
    else:
        print("* "+k*" "+"* "+j*" "+j*"* ")
        k+=1
        j+=1

"""
    elif i<=(num//2):
        print((num-3)*"* "+(num-3)*" "+" *")
    elif i>=(num//2):
        print("* "+(num-3)*" "+(num-3)*"* ")
   
"""