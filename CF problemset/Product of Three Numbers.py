import math

t = int(input())

for _ in range(t):
    n = int(input())
    m = int(math.sqrt(n)) + 2
    a, b, c = 0, 0, 0

    for i in range(2, m):
        if n % i == 0:
            a = i
            break
    
    if a == 0:
        print("NO")
        continue
    
    for i in range(a+1, m):
        if n % (a * i) == 0:
            b = i
            c = n // (a * b)
            if c != a and c != b and c >= 2:
                break
            else:
                c = 0

    if c:
        print("YES")
        print(a, b, c)
    else:
        print("NO")
