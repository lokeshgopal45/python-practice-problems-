"""
Abundant  Number:
Sum of their 'factors' is not Equal to the Given Number then it is called Abundant  Number


def abundant(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    if sum != number:
        return str(number) + ' is  Abundant Number '
    return str(number) + ' is not Abundant Number '


print(abundant(6))
"""


def finding_factors(number):
    factors =[]
    divisor = 2
    while divisor <= number:
        if number%divisor==0:
            factors.append(divisor)
            number /=divisor
        else:
            divisor+=1
    return factors
print(finding_factors(number))