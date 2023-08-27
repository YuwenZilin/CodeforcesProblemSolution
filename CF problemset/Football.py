n = int(input())

ans_dict = {}

for cases in range(n):
    x = input()
    ans_dict.setdefault(x, 0)
    ans_dict[x] += 1

print(max(zip(ans_dict.values(), ans_dict.keys()))[1])