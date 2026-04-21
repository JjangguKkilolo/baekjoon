N, M = map(int,input().split())
city = [list(map(int, input().split())) for _ in range(N)]

city_home = []
city_chicken = []

chicken_road = []

ans = int(1e10)

for i in range(len(city)):
    for j in range(len(city[i])):
        if city[i][j] == 1:
            city_home.append([i,j])
        elif city[i][j] == 2:
            city_chicken.append([i,j])

def solve(start, depth):
    global ans
    if depth == M:
        total_city_dist = 0

        for h_r, h_c in city_home:
            min_dist = 999999
            for idx in chicken_road:
                c_r, c_c = city_chicken[idx]
                dist = abs(h_r - c_r) + abs(h_c - c_c)
                min_dist = min(min_dist, dist)
    
            total_city_dist += min_dist
            
        ans = min(ans, total_city_dist)    
        return

    for i in range(start, len(city_chicken)):
        chicken_road.append(i)
        solve(i+1, depth+1)
        chicken_road.pop()

solve(0,0)
print(ans)
