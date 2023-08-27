n = int(input())
array = list(map(int,input().split()))
arraysorted = sorted(array.copy())
exchange = []
flag = False



for i in range(n):
    if array[i] != arraysorted[i]:
        exchange.append(i)
    
if exchange == []:
    flag = True
    exchange.append(0)
    exchange.append(0)
else:
    a = array.copy()[exchange[0]:exchange[-1]+1]
    a.reverse()
    if a == arraysorted[exchange[0]:exchange[-1]+1]:
        flag = True
    
if flag:
    print("yes")
    print(exchange[0]+1, exchange[-1]+1)
else:
    print("no")

