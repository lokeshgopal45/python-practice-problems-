"""
Reverse each word in a sentence
Given a long sentence, reverse each word of the sentence individually in the sentence itself.
Examples:

Input : Geeks For Geeks is good to learn
Output : skeeG roF skeeG si doog ot nrael

Input : Split Reverse Join
Output : tilpS esreveR nioJ
"""
string="Morgan Stanley"
temp=string.split()
ans=[" ".join(i[::-1]for i in temp)]
print(*ans)