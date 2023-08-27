from math import log

x = int(input())
n = 0

while x > 1:
    a = int(log(x,2))
    n += 1
    x -= 2**a

print(n+x)

