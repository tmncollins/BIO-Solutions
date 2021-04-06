from functools import lru_cache
from math import comb

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

def password(n, word, length):
    if length <= 0:
        return word
    if len(word) == 0:
        a = 0
    else:
        a = alpha.index(word[-1]) + 1

    for letter in range(a, len(alpha)):
        perms = comb(36 - letter - 1, length-1)
#        print(letter, perms, n, length)
        if n <= perms:
            return password(n, word + alpha[letter], length-1)
        n = n - perms

def getLength(n):
    l = 1
#    print(getLen(36, l))
#    while n > getLen(36, l):
    while n > comb(36, l):
        n -= comb(36, l)
        l += 1
    return l,n

n = int(input())

l,n = getLength(n)
print(password(n, "", l))

"""
b) 14, BIO, NTU, BIO14, ABCDE

c) 68719476734
passwords up to length of 36 will be accepted

d) There is only 1 pair that fulfills this criteria: ATUVWXYZ0123456789 and BCDEFGHIJKLMNOPQRS. Given a password,
the next password will either have the same number of digits or 1 more digit. For the number of digits between the 
passwords to be 36, without repeats, both passwords must contain 18 digits. As the passwords are ordered, the first
password must contain the A. As the second password cannot contain an A, the first password must be the last password 
beginning with A. 

"""

def c():
    ans = 0
    for length in range(1,36):
        ans += comb(36, length)
    print(ans)
