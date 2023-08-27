t = int(input())

for testcases in range(t):
    string = input()
    ans = 0

    for i in range(10):
        if string[i] != "codeforces"[i]:
            ans += 1
    
    print(ans)