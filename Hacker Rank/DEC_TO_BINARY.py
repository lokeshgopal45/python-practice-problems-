test=int(input())                           # Test case Input
for i in range(test):                       # up to that test cases
    sum = 0                                 # For Every answer we have to add that sum
    N=input()                               # Input
    N=N[::-1]                               # Reverse this input (1)
    for i in range(len(N)):                 # For loop for up to input length
        sum+=((2**int(i))*int(N[i]))        # Binary Value (2)
    print(sum)


# Note
"""
1: We calculate the Binary From LSB to MSB 
 Eg: Input=011
        1->1->0
2. We Normally calculate the Binary value just like this
        2**index*Value so
        Input =011
        1->1->-0 
        (2**0)* value---->(2**0)*1=1   
        (2**1)* value---->(2**1)*1=2
        (2**2)* value---->(2**1)*0=0
    ans would become 3 
    int for we take input as string so we have to convert to integer so type casting
"""
