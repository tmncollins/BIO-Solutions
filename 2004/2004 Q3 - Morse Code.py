import time
from functools import lru_cache

"""
NOTE THAT THIS SOLUTION IS A LITTLE BIT TOO SLOW IN SOME TEST CASES
"""

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
         ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
alpha = list("abcdefghijklmnopqrstuvwxyz")

toMorse = dict(zip(alpha, morse))
toAlpha = dict(zip(morse, alpha))

word = input()

start = time.time()

m = ""
for letter in word: m += toMorse[letter]
#print(m)

size = len(word)
check = True

#@lru_cache(maxsize=None)
def func(word, remainder):
    global m, check
    tot = 0
    if (len(remainder)) > (size - len(word)) * 4: return 0
    for i in range(min(4, len(remainder))):
        if remainder[:i+1] in morse:
            w = word + toAlpha[remainder[:i+1]]
            r = remainder[i+1:]
            if len(r) == 0:
                if  len(w) == size:
                    tot += 1
#                print(remainder, word)
            else:
                tot += func(w,r)
    return tot

print(func("", m))

print("Time:", time.time() - start)

"""
b) ----- = 13
   -..-----. = 170
c) 124
"""


