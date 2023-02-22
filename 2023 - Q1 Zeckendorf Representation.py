# get input
n = int(input())

def zeckendorf(n):

    # generate fib sequence up to n
    def gen_fib(n):
        a, b = 1, 1
        fib = [a, b]
        while a < n:
#            if sum(fib) == n: print("!")
            c = a + b
            b = a
            a = c
            fib.append(c)
#        print(sum(fib) - n - a)
        return fib

    fib_seq = gen_fib(n)
    # pointer to current index in fib sequence
    ptr = len(fib_seq) - 1
    ans = []

    # generate z sequence
    while n > 0:
        # can we use this number?
        if fib_seq[ptr] <= n:
            n -= fib_seq[ptr]
            ans.append(str(fib_seq[ptr]))
            # skip the next number
            ptr -= 1
        ptr -= 1

#    print(gen_fib(5000000000))
    return ans


ans = zeckendorf(n)

# output
print(" ".join(ans))

"""
1 (b) This is simply finding the largest number in the fib sequence < 1,000,000
ANS : 832040

"""

def n_seq(n):
    ans = []

    for i in range(1, n+1):
        z = zeckendorf(i)
        ans.append(str(len(z)))

    return ans

#n_seq(n)
"""

1 (c) Consider first 20 numbers in z representation
1 - 1   {1}             11 - 8 3    {2}
2 - 2   {1}             12 - 8 3 1  {3}
3 - 3   {1}             13 - 13     {1}
4 - 3 1 {2}             14 - 13 1   {2}
5 - 5   {1}             15 - 13 2   {2}
6 - 5 1 {2}             16 - 13 3   {2}
7 - 5 2 {2}             17 - 13 3 1 {3}
8 - 8   {1}             18 - 13 5   {2}
9 - 8 1 {2}             19 - 13 5 1 {3}
10- 8 2 {2}             20 - 13 5 2 {3}

Consider the n-sequence, the length of the nth z sequence. 
The sequence has been split so that each 1 starts a new line:
1 {1}
1 {1}
1 2 {2}
1 2 2 {3}
1 2 2 2 3 {5} 
1 2 2 2 3 2 3 3 {8}
1 2 2 2 3 2 3 3 2 3 3 3 4 {13}
1 2 2 2 3 2 3 3 [ 2 3 3 ] 3 4 2 3 3 3 4 3 4 4 {21}
1 2 2 2 3 2 3 3 2 3 3 3 4 2 3 3 3 4 3 4 4 2 3 3 3 4 3 4 4 3 4 4 4 5 {34}
The length of each line is a term in the fibonacci sequence
Now consider how many 3s are in each line:
0 0 0 0 1 3 6 10 15
These are the triangle numbers. 
Thus, we can use this information to determine how many numbers have a z sequence of length 3
53,316,291,173 is a fib number, making this easier

ANS : 18424
"""

# n must be a fibonacci number
def c(n):
    N = n
    n -= 7 # the first 7 terms contain no 3s
    tri = 1
    tri_incr = 2
    a, b = 3, 5
    ans = 0

    # work our way up the sequence
    while n >= b:
        n -= b
        c = a + b
        a = b
        b = c
        ans += tri
        tri += tri_incr
        tri_incr += 1

    print(ans)

#c(53316291173)

"""
The fib number after 701,408,733 is 

consider the numbers with 3 in their z sequence
3, 4, 11, 12, 16, 17, 24, 25, 32, 33, 37, 38, 45
 +1  +7  +1  +4  +1  +7  +1  +7  +1  +4  +1  +7

"""
