t = int(input())

for i in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()

    flag = True
    for k in range(n-1):
        if array[k] >= array[k+1]:
            flag = False
            break

    print("YES" if flag else "NO")



