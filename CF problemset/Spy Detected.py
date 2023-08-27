n = int(input())
ans=[]
for i in range(n):
    a = int(input())
    numlist = list(map(int,input().split()))
    valuelist = set(numlist)
    for j in valuelist:
        if numlist.count(j) == 1:
            ans.append(numlist.index(j)+1)
for i in ans:
    print(i)
