alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
conv = dict()
for i in range(26):
    conv[alpha[i]] = i+1

ans = ""

code = input().upper()
code = code[::-1]

for i in range(len(code) - 1):
    a = conv[code[i]] - conv[code[i+1]]
    if a <= 0: a += 26
    ans += alpha[a-1]

ans += code[-1]
ans = ans[::-1]
print(ans)