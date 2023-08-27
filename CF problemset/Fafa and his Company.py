employees = int(input())
ans = 0
for i in range(1,employees//2+1):
    if (employees-i)%i == 0:
        ans+=1
print(ans)