def solve(start, depth):
    if depth == M:
        print(*(result))
        return

    for i in range(start, N +1):
        result.append(i)
        solve(i+1, depth+1)
        result.pop()



N, M = map(int, input().split())
result= []

solve(1,0)
