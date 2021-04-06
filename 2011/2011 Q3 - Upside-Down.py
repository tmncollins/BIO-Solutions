n = int(input())

llist = list("123456789")
rlist = llist[::-1]

def func(n, left, right):
    if n == 0:
        return left + right
    if n == 1:
        return left + "5" + right

    m = 0
    while n >= 2 * 9**m:
        m += 1
#    m -= 1
    n -= 2
#    print(n, m, 9**m)
    left = llist[(n % 9)] + left
    right += rlist[(n % 9)]

    return func(n // 9, left, right)



print(func(n, "", ""))


"""
b) 8 * 6 * 4 * 2 = 384

c) 38, 54747259285257139791317935852815836365

d) More with 1001 digits. 1001 is an odd number and so every every upside-down number of that length has 5 as its middle
digit. 1000 is an even number and so not every upside-down number of that length will contain a 5. 

By adding a 5 to the centre of a 1000 digit upside-down number creates a 1001 digit upside-down number. Thus, each 
1000 digit upside-down number creates a specific 1001 digit upside-down number, meaning there are the same number of 
1000 digit and 1001 digit upside-down numbers.
"""