casenum = int(input())

for i in range(casenum):
    t = int(input())
    problems = input()
    ans = []
    balloons = 0

    for k in range(t):
        if problems[k] not in ans:
            balloons += 2
            ans.append(problems[k])
        else:
            balloons += 1
    
    print(balloons)



