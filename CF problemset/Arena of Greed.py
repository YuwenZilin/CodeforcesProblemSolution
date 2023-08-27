T = int(input())

'''
def takecoin(a):
    if a == 4:
        return 2
    elif a % 2 == 1:
        return 1
    elif a % 4 == 0:
        return 1
    else:
        return a//2
'''

for testcases in range(T):
    N = int(input())
    Chanek = 0
    flag = True


    while N > 0:
        takes = 0
        if N % 2 == 1:
            takes = 1
            N -= takes
        else:
            if N == 4:
                takes = 2
                N -= takes
            elif N % 4 == 0:
                takes = 1
                N -= takes
            else:
                takes = N//2
                N -= takes
        if flag:
            Chanek += takes
        flag = not(flag)

    print(Chanek)