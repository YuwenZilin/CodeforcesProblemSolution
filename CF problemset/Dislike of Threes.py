index = []
for i in range(1,3000):
    if i%3 == 0:
        a=1
    elif  "3" in str(i):
        a=1
    else:
        index.append(i)
a = int(input())
ans = []
for i in range(a):
    x = int(input())
    ans.append(index[x-1])
for i in ans:
    print(i)