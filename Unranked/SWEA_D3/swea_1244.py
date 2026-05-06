def dfs(index):
    global max_score
    current_score = "".join(score)
    if (index, current_score) in visited:
        return
    visited.add((index, current_score))

    if index == change_count:
        max_score = max(max_score, int(current_score))
        return
    n = len(score)
    for i in range(n-1):
        for j in range(i+1,n):
            score[i], score[j] = score[j], score[i]
            dfs(index + 1)
            score[i], score[j] = score[j], score[i]
    

T = int(input())

for test_case in range(1,T+1):
    score ,change_count = map(int,input().split())
    score = list(str(score))
    max_score = -1e10
    visited = set()

    dfs(0)
    print(f"{test_case} {max_score}")
    
    
    
    
    
