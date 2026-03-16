from collections import deque

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_decks(n, c, s, debug=False):
    cards = []
    for i in range(n):
        cards.append(ALPHA[i])
        cards.append(ALPHA[i])

    for i in range(s):
        A, B = cards[:n][::-1], cards[n:][::-1]
        if debug: print(cards, A, B)
        new_cards = deque()
        for _ in range(n):
            new_cards.append(B.pop())
            new_cards.append(A.pop())
        if debug: print(new_cards)
        new_cards.rotate(-c)
        if debug: print(new_cards)
        cards = list(new_cards)

    alpha = []
    beta = []
    for i in cards:
        if i in alpha: beta.append(i)
        else: alpha.append(i)

    return alpha, beta

def encrypt(alpha, beta, string):
    alpha = list(alpha)
    beta = list(beta)
    output = ''
    middle = n // 2

    for l in string:
        # encrypt
        while alpha[0] != l:
            alpha.append(alpha.pop(0)) # top card placed on bottom
            beta.append(beta.pop(0)) # top card placed on bottom
        output += beta[0]
        # manipulate
        alpha.insert(middle, alpha.pop(1)) # 2nd card placed in middle
        beta.append(beta.pop(0)) # top card placed on bottom
        beta.insert(middle, beta.pop(2)) # 3rd card placed in middle
#        print(''.join(alpha), ''.join(beta))

    return output

n, s, c, word = input().strip().split()
n = int(n)
s = int(s)
c = int(c)

alpha, beta = generate_decks(n,c,s)

# print(''.join(alpha), ''.join(beta))

print(encrypt(alpha, beta, word))

"""
b) LOUDER

c) BETA: QBDPOACNMHLKGFJIE gives encrypted QPONMLKJIHGFEQDOC

d) 54 
"""