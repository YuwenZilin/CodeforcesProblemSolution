t = int(input())

for testcaases in range(t):
    n, k = map(int,input().split())
    a = k//(n-1)

    if k%(n-1) == 0:
        print(n*a-1)
    else:
        print(n*a+k%(n-1))

