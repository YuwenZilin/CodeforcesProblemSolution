import math

n = int(input())
flowers = list(map(int,input().split()))

flowers.sort()
a, b = 0, 0

if flowers[0] == flowers[-1]:
    print(0, math.comb(n, 2))

else:
    for i in range(n):
        if flowers[i] == flowers[0]:
            a += 1
        elif flowers[i] == flowers[-1]:
            b += 1

    print(flowers[-1]-flowers[0], a*b) 