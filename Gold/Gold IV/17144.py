def dust_spread():
    move = [[0] *C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j]>=5:
                d = board[i][j]//5
                for dx, dy in (-1, 0), (1,0), (0,1), (0,-1):
                    ni, nj = i+dx, j+dy
                    if 0<=ni<R and 0<=nj<C and board[ni][nj] != -1:
                        move[ni][nj] += d
                        board[i][j] -= d
    for i in range(R):
        for j in range(C):
            board[i][j] += move[i][j]

def air_cleaner(start, dir):
    if dir == -1:
        for i in range(start-1,0,-1):
            board[i][0] = board[i-1][0]
        for j in range(0,C-1):
            board[0][j] = board[0][j+1]
        for i in range(0,start):
            board[i][C-1] = board[i+1][C-1]
        for j in range(C-1,1,-1):
            board[start][j] = board[start][j-1]
    else:
        for i in range(start+1,R-1):
            board[i][0] = board[i+1][0]
        for j in range(0,C-1):
            board[R-1][j] = board[R-1][j+1]
        for i in range(R-1,start,-1):
            board[i][C-1] = board[i-1][C-1]
        for j in range(C-1,1,-1):
            board[start][j] = board[start][j-1]
    board[start][1] = 0

R, C, T = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(R)]
cleaner = []
for i in range(R):
    if board[i][0]==-1:
        cleaner.append(i)
        cleaner.append(i+1)
        break

for _ in range(T):
    dust_spread()
    air_cleaner(cleaner[0], -1)
    air_cleaner(cleaner[1], 1)

board[cleaner[0]][0], board[cleaner[1]][0] = 0, 0
print(sum(map(sum,board)))
