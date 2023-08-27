t = int(input())

for i in range(t):
    n = int(input())
    row1 = [x for x in input()]
    row2 = [x for x in input()]

    for k in range(n):
        if row1[k] == "B":
            row1[k] = "G"
        if row2[k] == "B":
            row2[k] = "G"
        
    print("YES" if row1 == row2 else "NO")