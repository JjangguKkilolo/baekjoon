count, cal_limit = map(int, input().split())
N = list(list(map(int, input().split())) for _ in range(count))

max_score = 0

def dfs(index, current_score, current_cal):
    global max_score
    
    if current_cal > cal_limit:
        return
    
    if index == count:
        max_score = max(max_score, current_score)
        return

    dfs(index +1, current_score + N[index][0], current_cal + N[index][1])
    dfs(index +1, current_score, current_cal)

dfs(0,0,0)
print(max_score)


