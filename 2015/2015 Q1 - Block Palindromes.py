import time

seen = set()
allSeen = set()
def palindrome(blocks):
    done = True

    b = tuple(blocks)
    if b in allSeen:
        return blocks

    allSeen.add(b)


    if blocks == blocks[::-1]:
        seen.add(b)

    for item in blocks:
        if len(item) > 1:
            done = False
            break
    if done:
        return blocks

    for i in range(len(blocks)):
        for j in range(1,len(blocks[i])):
            new = list(blocks)
            w = new.pop(i)
            a = w[:j]
            b = w[j:]
            new.insert(i, b)
            new.insert(i, a)
            palindrome(new)

a = input()
start = time.time()
palindrome([a])
print(seen)
print(len(seen) - 1)
print("Time:", time.time() - start)

"""
b) ('A', 'ABCBA', 'A'), 
   ('AA', 'BCB', 'AA'), 
   ('AA', 'B', 'C', 'B', 'AA'), 
   ('A', 'A', 'B', 'C', 'B', 'A', 'A'), 
   ('A', 'A', 'BCB', 'A', 'A')
   
c) If all the groupings contain an even number of block, then the block palindrome contains an even number of letters.
When a block palindrome is reversed, each block in the first half of the word is repeated in the second half. So there
are 2 * n blocks, which is even. Also, there must only be 1 possible grouping. If there is more than 1 possible grouping,
then at least grouping must contain more than 2 blocks. Any grouping that contains more than 2 blocks can be changed into 
a grouping with the first block, the last blocks and the other blocks grouped into 1 block, which gives an odd number of
blocks.

"""



