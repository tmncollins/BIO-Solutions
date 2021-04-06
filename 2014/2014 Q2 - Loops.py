
# 0 - up, 1 - right, 2 - down, 3 - left
# 0 red, 1 green
tiles = [[(0,2), (1,3)], [(1,3), (0,2)], [(0,3), (1,2)], [(0,1), (2,3)], [(2,1), (0,3)], [(2,3), (0,1)]]
opposite = {0:2, 2:0, 1:3, 3:1}
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

#print(board)

# score loops
def countLoop(player):
    seen = set()
    score = 0
    for Y in range(n):
        for X in range(n):
            x = X
            y = Y
            if (x,y) not in seen:
                loop = set()
                complete = False
                t = board[y][x]
                move = tiles[t-1][player][1]
                while True:
                    seen.add((x, y))
                    if (x,y) in loop:
                        complete = True
                        break
                    loop.add((x,y))
                    if move == 0:
                        # up
                        y -= 1
                        if y < 0: break
                        if opposite[move] in tiles[board[y][x]-1][player]:
                            a = tiles[board[y][x]-1][player][0]
                            if a == opposite[move]:
                                a = tiles[board[y][x]-1][player][1]
                            move = a
                        else:
                            break
                    elif move == 1:
                        # right
                        x += 1
                        if x >= n: break
                        if opposite[move] in tiles[board[y][x]-1][player]:
                            a = tiles[board[y][x]-1][player][0]
                            if a == opposite[move]:
                                a = tiles[board[y][x]-1][player][1]
                            move = a
                        else:
                            break
                    elif move == 2:
                        # down
                        y += 1
                        if y >= n: break
                        if opposite[move] in tiles[board[y][x]-1][player]:
                            a = tiles[board[y][x]-1][player][0]
                            if a == opposite[move]:
                                a = tiles[board[y][x]-1][player][1]
                            move = a
                        else:
                            break
                    elif move == 3:
                        # left
                        x -= 1
                        if x < 0: break
                        if opposite[move] in tiles[board[y][x]-1][player]:
                            a = tiles[board[y][x]-1][player][0]
                            if a == opposite[move]:
                                a = tiles[board[y][x]-1][player][1]
                            move = a
                        else:
                            break
                if complete:
                    score += len(loop)

    return score

print(countLoop(0), countLoop(1))

"""
b) 31
Any of the 6 tiles in the red loop can be switched with a different tile to break the loop (6 * 5)
Also, the one missing tile in the green loop can be placed to increase green's score (1)

c) 18
16 can be scored either by a sum of a number of loops: 4, 6, 8, 10, 12, 14, 16. 
16 - 4 + 2 = 6
12+4 - 4 + 1 = 5
4+4+4+4 - 1 = 1
10+6 - This cannot be done
8+8 - 2 = 2
4+4+8 - 4 = 4
total = 18

d) No. Every time a line moves left in a loop it must move right again, similarly for up and down. Therefore, each
loop must contain an even number of tiles. So each player's score must be an even number, and the difference between
them must also always be even. 

"""

