from functools import lru_cache
from time import time

n = int(input())

@lru_cache(maxsize=None)
def count_raindrops(length, maximum=None, last_digit=0, dropped=False):
    if length == 0: return int(dropped)

    if maximum:
        ans = 0
        m = int(maximum[0])
        for i in range(0, m):
            if i < last_digit:
                if not dropped: ans += count_raindrops(length-1, None, i, True)
            else: ans += count_raindrops(length-1, None, i, dropped)

        if m >= last_digit or (not dropped):
            ans += count_raindrops(length-1, maximum[1:], m, dropped or (m < last_digit))
        return ans

    else:
        ans = 0
        for i in range(0, 10):
            if i < last_digit:
                if not dropped: ans += count_raindrops(length - 1, None, i, True)
            else:
                ans += count_raindrops(length - 1, None, i, dropped)
        return ans

def count_raindrops_dp(n):
    length = len(str(n))
    ans = count_raindrops(length, str(n))
    return ans

def is_raindrop(i):
    i = str(i)
    drops = 0
    for j in range(len(i)-1):
        if i[j+1] < i[j]: drops += 1
    return drops == 1

def count_raindrops_naive(n):
    ans = 0
    for i in range(1, n+1):
#        if is_raindrop(i): print(i)
        ans += is_raindrop(i)
    return ans

start_time = time()

print(count_raindrops_dp(n))
print(time() - start_time)

print(count_raindrops_naive(n))
print(time() - start_time)

def b(i):
    while True:
        i += 1
        if is_raindrop(i): return i

def c(n):
    upper = 2
    while count_raindrops_dp(upper) < n:
#        print(upper, count_raindrops_dp(upper), n)
        upper *= 2
    lower = upper // 4

    # binary search
    while upper > lower+1:
        print(upper, lower)
        mid = (upper + lower) // 2
        x = count_raindrops_dp(mid)
        if x < n:
            lower = mid+1
        elif x > n:
            upper = mid-1
        else:
            upper = mid
    if count_raindrops_naive(lower) == n and is_raindrop(lower): return lower
    return upper

#print(c(12345))
#print(is_raindrop(144799112334555556799))

def different_digits(a,b):
    a = str(a); b = str(b)
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]: diff += 1
    return diff

def d(length):
    start = pow(10, length-1)
    end = pow(10, length)
    raindrops = []
    for i in range(start, end):
        if is_raindrop(i): raindrops.append(i)
    count = 0
#    print(len(raindrops))
    for i in range(len(raindrops)-1):
        if different_digits(raindrops[i], raindrops[i+1]) == length-1: count += 1
    return count

#print(c(10000000000))
for i in range(1, 10):
    print(i, d(i))



"""
b) 8111111

c) 112444777888822225

d) 7974
0 + 37 + 80 + 81 * (100-3) = 7974
 """
