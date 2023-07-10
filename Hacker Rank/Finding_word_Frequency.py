Input ="""
John is the son of John second
Second son of John second is William second."
"""
from collections import Counter
Counter=Counter(Input.split())
ans=Counter.most_common(5)
print(ans)