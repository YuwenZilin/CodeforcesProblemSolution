a = input()
b = list(i for i in a)
decode = []
while b != []:
    if b[0] == ".":
        decode.append("0")
        b.pop(0)
    elif b[0] == "-" and b[1] == ".":
        decode.append("1")
        del b[:2:]
    else:
        decode.append("2")
        del b[:2:]
print("".join(decode))