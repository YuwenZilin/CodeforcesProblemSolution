n = int(input())
array = list(map(int,input().split()))

ans = [1]*n
for i in range(n-1):
    if array[i] < array[i+1]:
        ans[i+1] = ans[i]+1

print(max(ans))