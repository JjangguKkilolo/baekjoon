T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    sum_flies = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            sum_flies[i][j] = board[i-1][j-1] + sum_flies[i-1][j] + sum_flies[i][j-1] - sum_flies[i-1][j-1]
            
    max_flies = 0

    for i in range(M, N + 1):
        for j in range(M, N + 1):
            current_sum = sum_flies[i][j] - sum_flies[i-M][j] - sum_flies[i][j-M] + sum_flies[i-M][j-M]
            if current_sum > max_flies:
                max_flies = current_sum

    print(f"#{test_case} {max_flies}")
        
