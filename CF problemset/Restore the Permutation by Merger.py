t = int(input())

for testcases in range(t):
    n = int(input())
    merging_permutation = list(map(int,input().split()))
    a = 0
    permutation = []

    for i in merging_permutation:
        if i not in permutation:
            print(i, end=" ")
            permutation.append(i)
            a += 1
        if a == n:
            print("\n")
            break
