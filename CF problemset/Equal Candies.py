testnum = int(input())

for i in range(testnum):
    t = int(input())
    box = list(map(int,input().split()))
    ans = 0

    for j in range(t):
        ans += (box[j]-min(box))
    
    print(ans)

