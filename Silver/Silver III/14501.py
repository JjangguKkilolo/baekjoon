N = int(input())
T = [list(map(int,input().split())) for _ in range(N)]

memo = [-1] * (N+1)

def max_profit(day):
    if day >= N:
        return 0

    if memo[day] != -1:
        return memo[day]

    res = max_profit(day+1)

    time, pay = T[day]
    if day + time <=N:
        res = max(res, pay + max_profit(day+ time))

    memo[day] = res
    return res

print(max_profit(0))
    
