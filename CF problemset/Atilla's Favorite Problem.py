t = int(input())

for i in range(t):
    n = int(input())
    string = input()
    alpahbetbox = set()
    for k in string:
        alpahbetbox.add(ord(k))
    print(max(alpahbetbox)-ord("a")+1)

