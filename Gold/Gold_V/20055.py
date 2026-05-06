from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
belt = deque(map(int, sys.stdin.readline().split()))

robots = deque([0] * N)

result = 1
while True:
    #1
    belt.rotate(1)
    robots.rotate(1)
    robots[N-1] = 0
    #2
    for i in range(N-2, -1, -1):
        if robots[i] == 1:
            if robots[i+1] == 0 and belt[i+1]>=1:
                robots[i+1] = 1
                robots[i] = 0
                belt[i+1] -= 1

                if i+1 == N-1:
                    robots[i+1] = 0

    #3
    if belt[0]>0:
        robots[0] = 1
        belt[0]-= 1

    #4
    if belt.count(0) >= K:
        break
    else:
        result +=1

print(result)
