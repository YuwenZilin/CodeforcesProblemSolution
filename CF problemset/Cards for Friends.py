for i in range(int(input())):
    w,h,n = map(int,input().split())
    pieces = 1
    while w%2 == 0:
        w = w//2
        pieces = pieces*2
    while h%2 == 0:
        h = h//2
        pieces = pieces*2
    print("YES" if pieces >= n else "NO")