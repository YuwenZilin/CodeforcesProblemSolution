n = int(input())
boys = list(map(int,input().split()))
m = int(input())
girls = list(map(int,input().split()))

boys.sort()
girls.sort()

ans = 0
pointerboys = 0
pointergirls = 0
while n > pointerboys and m > pointergirls:
    for i in range(pointergirls,m):
        if abs(boys[pointerboys]-girls[i]) <= 1:
            ans += 1
            pointergirls = i+1
            break
    pointerboys += 1

print(ans)


