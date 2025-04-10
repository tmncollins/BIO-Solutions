from time import time

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    x = n
    if not is_palindrome(x):
        if len(str(x)) % 2 == 1:
            x = str(x)
            x = x[:len(x)//2+1]
            y = x[:-1]
            x = int(x + y[::-1])
        else:
            x = str(x)
            x = x[:len(x)//2]
            x = int(x + x[::-1])
    if str(x).count("9") == len(str(x)):
        return next_palindrome(x+1)

    while x <= n:
        x = increment_palindrome(x)
    return x

def increment_palindrome(x):
    # increment middle number
    x = list(str(x))
    i = (len(x)-1)//2
    while True:
        if x[i] != "9":
            inc = str(int(x[i])+1)
            x[i] = x[len(x)-1-i] = inc
            return int("".join(x))
        else:
            x[i] = x[len(x)-1-i] = "0"
            i -= 1

n = int(input())
start = time()

palindromes = []
i = 1
while i <= n:
    palindromes.append(i)
    i = next_palindrome(i)
print(len(palindromes))
print(time() - start)

def find_sum(n, length, d=1):
    if length <= 0:
        return False
    if n <= 0:
        return False
    if is_palindrome(n):
        return [n]

    i = 0
    if d == -1: i = len(palindromes)-1
    for _ in range(len(palindromes)):
        x = find_sum(n-palindromes[i], length-1, -1)
        if x: return [palindromes[i]] + x
        i += d

    return False

def palindromic_sum(n):
    if is_palindrome(n): return [n]
    x = find_sum(n, 2)
    if x: return x
    return find_sum(n, 3)

sum = palindromic_sum(n)
sum = sorted(sum)
for i in sum: print(i, end=" ")
print()
print(time() - start)
print()

def c(max_number):
    p = set()
    palindromes = []
    i = 1
    while i <= max_number:
        palindromes.append(i)
        p.add(i)
        i = next_palindrome(i)
    for a in palindromes:
        for b in palindromes:
            if a+b <= max_number:
                p.add(a+b)
    print(max_number - len(p))

c(1000000)

"""
b)
1 9 44
2 8 44
3 7 44
4 6 44
5 5 44

c) 266948
"""
