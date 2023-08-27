t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    if n%2 == 0:
        print(n//2*m)
    elif m%2 == 0:
        print(m//2*n)
    else:
        print(n//2*m+m//2+1)