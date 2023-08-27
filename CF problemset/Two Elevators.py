t = int(input())

for i in range(t):
    a, b, c = map(int,input().split())
    timefirst = abs(a-1)
    timesecond = abs(b-c) + abs(c-1)
    if timefirst < timesecond:
        print(1)
    elif timefirst > timesecond:
        print(2)
    else:
        print(3)
    
