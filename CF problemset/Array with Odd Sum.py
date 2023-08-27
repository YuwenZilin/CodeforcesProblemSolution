t = int(input())

for i in range(t):
    n = int(input())
    array = list(map(int,input().split()))

    flagodd=False
    flageven=False

    for k in range(n):
        if array[k]%2 == 0:
            flageven = True
        else:
            flagodd = True
        if flagodd and flageven:
            break

    if flagodd and flageven:
        print("YES")
    elif flagodd == False:
        print("NO")
    elif flagodd == True:
        print("NO" if n%2 == 0 else "YES")

