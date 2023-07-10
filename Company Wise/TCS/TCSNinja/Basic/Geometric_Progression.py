limit=30
Num=int(input())
series=[]
odd=1
even=2

# Even GP
First_CR,first_term,second_term=2,1,2
# Odd GP
Second_CR,first_term,second_term=3,1,3
for i in range(limit+1):
    series.insert(odd,first_term*First_CR**i)
    series.insert(even,first_term*Second_CR**i)
    odd+=2
    even+=2
#series=series[1:]
print(series)
print(series[Num-1])