casenum = int(input())

for i in range(casenum):
    n = int(input())
    numset = list(map(int,input().split()))
    oddnum = 0
    
    for k in numset:
        if k % 2 == 0:
            oddnum += 1

    print("YES" if oddnum == n else "NO")