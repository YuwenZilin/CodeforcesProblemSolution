t = int(input())

for testcases in range(t):
    integers = list(map(int,input().split()))
    integers.sort(reverse=True)
    if integers[0] == integers[1] and integers[1] != integers[2]:
        print("YES")
        print(integers[0],integers[2],1)
    elif integers[0] == integers[1] and integers[1] == integers[2]:
        print("YES")
        print(integers[0],integers[0],integers[0])
    else:
        print("NO")

