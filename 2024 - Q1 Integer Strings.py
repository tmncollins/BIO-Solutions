from math import *
from time import time

def count_len_below_2(n, x):
    return (n)*x

def count_len_below(n):
    if n < 10: return n
    i = 1
    l = 1
    ans = 0
    while i*10 <= n:
        ans += 9*(i)*(l)
        i *= 10
        l += 1
#        print(i, l, n, ans)
    ans += ((n//i)-1)*(i)*(l)
#    print(ans)
    ans += count_len_below_2(n%i+1, len(str(n)))
    return int(ans)

def count_brute(n):
    string = ""
    for i in range(1, n):
        string += str(i)
    return len(string)

def find_brute(start, n):
    string = ""
    i = start
    while len(string) < n:
        string += str(i)
        i += 1
    return string[n-1]

def get_nth(i):
    MIN = 1
    MAX = int(pow(2, 64))
    while MIN < MAX:
        HALF = (MAX + MIN) // 2
#        print(MIN, MAX, HALF)
        if i > count_len_below(HALF):
            MIN = HALF + 1
        else:
            MAX = HALF
    i -= count_len_below(MIN-1) + 1
    return str(MIN)[i]

n, j = list(map(int, input().split()))
start = time()
i = j+count_len_below(n-1)
print(get_nth(i))
print("Time taken:", time() - start)
#print(find_brute(n, j))

"""
b) 12
c) 11111 occurs first at 110 [111 11]2
There are 222 digits to the left of 111, so the substring first occurs between 223-227

987654321 occurs first at 1[98765432 1]987654323
There are 1677777777 digits to the left of 198765432, so the substring first occurs between 1677777779 and 1677777787
"""

def b(length, digit):
    i = 1
    s = ""
    while len(s) < length:
        s += str(i)
        i += 1
    s = s[:length]
    return s.count(str(digit))

#print(b(101, 5))

def c(substring):
    substring = str(substring)
    s = ""
    i = 1
    while substring not in s:
        s += str(i)
        i += 1
    return s.index(substring)

#print(c(11111))

