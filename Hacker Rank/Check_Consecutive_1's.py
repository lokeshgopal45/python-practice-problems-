"""
Check if there are K consecutive 1’s in a binary number
Given K and a binary number, check if there exists k consecutive 1’s in the binary number.

Examples:
Input : binary number = 101010101111,k = 4
Output : yes
Explanation: at the last 4 index there exists 4 consecutive 1's

Input : binary number = 11100000,k=5
Output : no
Explanation: There is a maximum of 3 consecutive 1's in the given binary.
"""
x,y=input().split(" ")      # Input Binary Value,Check Value
One=int(y)*"1"              # it is in string So type casting and multiply with "1"s
if One in x:                # Search in x for "1"s
    print("Yes")            # If it is Found print "yes"
else:                       # Else Print "No"
    print("No")