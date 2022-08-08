import math
from wsgiref.validate import InputWrapper
input = 69
xwe = input
power = 0
x = 0
y = 0

def highest_power(inp):
    power = 0
    while pow(2, power + 1) <= inp:
        power += 1
    return power

outpustlist = []
while input != 0:
    power = pow(2, highest_power(input))
    outpustlist.append(power)
    input = input - power
print(outpustlist)

outpustlist.sort()
testlist = []
while highest_power(input) <= input:
    if pow(2,x) == outpustlist[len(outpustlist)-y-1]:
        testlist.append("1")
        x += 1
        y += 1
    elif pow(2,x) != outpustlist[len(outpustlist)-y-1]:
        testlist.append("0")
        x += 1
    print(testlist)
print(testlist)