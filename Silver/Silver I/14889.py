N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
min_s = 1e10

def backtrack(depth, index):
    global min_s

    if depth == N // 2:
        team_a, team_b = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team_a += S[i][j]
                elif not visited[i] and not visited[j]:
                    team_b += S[i][j]

        
        min_s = min(min_s, abs(team_a - team_b))
        return

    for i in range(index, N):
        if not visited[i]:
            visited[i] = True
            backtrack(depth+1, i+1)
            visited[i] = False


backtrack(0, 0)
print(min_s)
