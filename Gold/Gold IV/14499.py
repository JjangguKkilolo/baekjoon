# 1동 2서 3북 4남
def roll_dice(dir):
    global x, y
    
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    
    for i in move:
        nx, ny = x+dx[i], y+dy[i]

        if not (0<=nx<N and 0<= ny < M):
            continue

        x, y = nx, ny
        if i == 1:
            roll_east(dice)
        if i == 2:
            roll_west(dice)
        if i == 3:
            roll_north(dice)
        if i == 4:
            roll_south(dice)
            
        if board[x][y] == 0:
            board[x][y] = dice[6]
        else:
            dice[6] = board[x][y]
            board[x][y] = 0
            
        print(dice[1])

# 1위 2뒤 3오 4왼 5앞 6밑
def roll_east(dice):
    dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]

def roll_west(dice):
    dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]

def roll_north(dice):
    dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]

def roll_south(dice):
    dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]


N, M, x, y, K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
move = list(map(int,input().split()))
dice = [0]*7

roll_dice(move)
