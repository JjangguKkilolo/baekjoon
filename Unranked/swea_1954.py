T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    y, x = 0, 0
    dist = 0
    print(f"#{test_case}")
    for i in range(1, N*N+1):
        board[y][x] = i
        ny = y + dy[dist]
        nx = x + dx[dist]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] != 0:
            dist = (dist+1)%4
            ny = y + dy[dist]
            nx = x + dx[dist]
        y , x = ny, nx
    for row in board:
        print(*row)
