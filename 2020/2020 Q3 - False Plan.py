from functools import lru_cache
import time

letters = ""
alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
row = 2

order = []
@lru_cache(maxsize=None)
def plan(last, n):
    global letters, row
#    print(last,n,row)

    if len(last) > row: return 0
    if n == 0:
#        print(tot)
        return 1
    ans = []
    for l in letters:
        if len(last) > 0 and l == last[0]:
            if len(last) < row:
                ans.append(plan(last + l, n-1))
        else:
            ans.append(plan(l, n-1))
    return sum(ans)

p,q,r = list(map(int, input().split()))
letters = alpha[:p]
row = q
n = int(input())
start = time.time()

def build(word, curr, n, length):
    global letters, row, p, q, r
    if len(word) == r: return word
#    print(word)
    for l in letters:
        a = curr + l
        if l not in curr: a = l
        if n <= plan(a, length-1):
            if len(curr) <= row:
                return build(word + l, a, n, length-1)
#            else: n += 1
        else:
            n -= plan(a, length-1)
    return word

print(plan("", "", r))
print(build("", "", n, r))
print("Time:", time.time() - start)

"""
b) 39, 29947
   
c) If a plan is in the same position when ordered forwards or backwards, the number of letters used (p) must be odd. The
nth plan must right at the middle of the list if its position is the same when ordered forwards or backwards, so there 
must be an odd number of plans. However, the length of the list of plans which contain more than 1 letter will always be
even. Also, r <= q, in order to achieve the length of plans so that they only contain 1 letter each. 
"""
