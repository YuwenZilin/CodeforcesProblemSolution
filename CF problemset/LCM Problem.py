t = int(input())

for testcases in range(t):
    l, r = map(int,input().split())
    
    if r >= l*2:
        print(l, l*2)
    else:
        print(-1,-1)