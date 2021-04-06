number = input()

convert = {"pa": "1", "vo":"4", "ze":"7", "re":"2", "mu":"5", "bi":"8", "no":"0", "ci":"3", "xa":"6", "so":"9"}
reverse = {"1":"pa","2":"re","3":"ci","4":"vo","5":"mu","6":"xa","7":"ze","8":"bi","9":"so","0":"no"}

ans = ""
for i in range(0, len(number), 2):
    ans += convert[number[i:i+2]]

print(ans)

# part c
"""
alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
for i in range(1, 10000):
    I = str(i)
    n = ""
    for q in I: n += reverse[q]
    tot = 0
    for l in n:
        tot += alpha.index(l) + 1
    if tot == i:
        print(n)
"""


"""
b) 94 + 26 = 120 = pareno
c) vobi, mupa


"""