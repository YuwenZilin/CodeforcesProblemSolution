import math

def combination2(a):
    if a >= 2:
        return(math.comb(a, 2))
    else:
        return(0)

n, m = map(int,input().split())

kmax = combination2(n - (m - 1))
if m == 1:
    kmin = kmax
else:
    if n % m == 0:
        kmin = m * combination2(n//m)
    else:
        a = n//m
        b = n - a * m
        kmin = (m - b) * combination2(a) + b * combination2(a+1)

print(kmin, kmax)
