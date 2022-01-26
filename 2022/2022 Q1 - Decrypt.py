alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
conv = dict()
for i in range(26):
    conv[alpha[i]] = i + 1

def decrypt(code):

    ans = ""
    code = code[::-1]

    for i in range(len(code) - 1):
        a = conv[code[i]] - conv[code[i+1]]
        if a <= 0: a += 26
        ans += alpha[a-1]

    ans += code[-1]
    ans = ans[::-1]
    return ans

def encrypt(code):

    ans = code[0]

    for i in range(1, len(code)):
        a = conv[code[i]] + conv[ans[-1]]
        if a > 26: a -= 26
        ans += alpha[a-1]

    return ans

def count_cycle(code):
    word = encrypt(code)
    i = 1
    while word != code:
        word = encrypt(word)
        i += 1
    return i

code = input().upper()
print(encrypt(code))
code = encrypt(code)
print(decrypt(code))

# c)
#print(count_cycle("OLYMPIAD"))

def d():
    num = 999999999999
    ans = 0
    for l1 in alpha:
        for l2 in alpha:
            for l3 in alpha:
                word = l1 + l2 + l3
                cycle = count_cycle(word)
                if num % cycle == 0: ans += 1
    print(ans)

#d()
