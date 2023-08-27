n, k = map(int,input().split())
strings = input()
ans = set()
i = 0


for i in range(n-k+1):
        print(i,i+k,int(strings[i:i+k],2))
        ans.add(int(strings[i:i+k],2))

print(ans)
print(len(ans))