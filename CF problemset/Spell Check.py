for i in range(int(input())):
    a = int(input())
    name = input()
    check = []
    for x in name:
        check.append(x)
    check.sort()
    print("YES" if check == ['T', 'i', 'm', 'r', 'u'] else "NO")







