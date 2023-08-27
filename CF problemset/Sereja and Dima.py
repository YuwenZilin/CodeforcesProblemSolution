n = int(input())
card = list(map(int,input().split()))
gamelist = []
for i in range(n):
    gamelist.append(max(card[0],card[-1]))
    if card[0] > card[-1]:
        card.pop(0)
    else:
        card.pop(-1)
Serja , Dima = 0 , 0
for i in gamelist[::2]:
    Serja += i
for i in gamelist[1::2]:
    Dima += i
print(Serja,Dima)