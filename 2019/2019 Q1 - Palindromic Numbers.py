def startPalindrome(n):
#    print(n)
    n = str(n)
    if len(n) == 1: return n
    p = ""
    for i in range(len(n) // 2):
#        a = max(int(n[i]), int(n[-(i+1)]))
        p += n[i]

    if len(n) % 2 == 1:
        return p + n[(len(n) // 2) + 1] + p[::-1]
    return p + p[::-1]

def improvePalindrome(number, i, n):
#    print(number)
    if int("".join(number)) > n:
        return "".join(number)
    a = int(number[i]) + 1
    if a > 9:
        number[i] = "0"
        number[-(i+1)] = "0"
        if i == 0:
            number = "".join(number)
            number = int(number) + 1
            number = startPalindrome(number)
            i = len(number) // 2
            return improvePalindrome(number, i, n)
        return improvePalindrome(number, i-1, n)
    number[i] = str(a)
    number[-(i+1)] = str(a)

    return improvePalindrome(number, i, n)

n = int(input())
q = startPalindrome(n+1)
#print(n, q)
c = len(q) // 2
print(improvePalindrome(list(q), c, n))

"""
b) 11 000 000 000
   99 999 999 999 999 999 999 - 99 999 999 988 999 999 999 = 11 000 000 000

c) 9030

"""

def generatePalindromes(n):
    palindromes = []
    for i in range(0,n):
        a = str(i) + str(i)[::-1]
        palindromes.append(int(a))
        a = list(a)
        a.pop(len(a) // 2)
        palindromes.append(int("".join(a)))
    return palindromes

def c():
    m = 100000
    nums = set()
    palindromes = generatePalindromes(m // 100)
#    print(palindromes)
    for a in palindromes:
#        print(a)
        for b in palindromes:
#            print(a+b)
            if a <= b and a+b < m:
                nums.add(a+b)
    print(m - len(nums))
#c()

