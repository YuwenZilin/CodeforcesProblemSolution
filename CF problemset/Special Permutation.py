casenum = int(input())

for i in range(casenum):
    n = int(input())
    index = [0]*n
    index[0] = n

    for k in range(1,n):
        index[k] = k
    
    for x in index:
        print(x,end=" ")
