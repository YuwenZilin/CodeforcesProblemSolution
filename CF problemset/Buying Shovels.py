import math

t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    a = n

    for i in range(1, int(math.sqrt(n)) + 2):
        if n % i == 0:
            if n // i <= k:
                a = min(a, i)
            elif i <= k:
                a = min(a, n//i)

    print(a)