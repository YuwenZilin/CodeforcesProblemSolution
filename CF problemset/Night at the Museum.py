name = input()
spell = "a"+name
ans = 0

for i in range(1,len(spell)):
    ans += min(abs(ord(spell[i])-ord(spell[i-1])),abs(26-abs(ord(spell[i])-ord(spell[i-1]))))

print(ans)

