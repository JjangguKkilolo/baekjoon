import sys
from collections import deque

gears = [deque(map(int, sys.stdin.readline().strip())) for _ in range(4)]
N = int(input())
rot = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]



#1일경우 시계 방향 -1일경우 반시계 방향
def gears_rotate(index, rot_dir):
    gears[index].rotate(rot_dir)

for target_idx, target_dir in rot:
    final_dirs = [0,0,0,0]
    final_dirs[target_idx - 1] = target_dir

    cur_idx = target_idx -1

    for i in range(cur_idx, 3):
        if gears[i][2] != gears[i+1][6]:
            final_dirs[i+1] = -final_dirs[i]
        else:
            break
    for i in range(cur_idx, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            final_dirs[i-1] = -final_dirs[i]
        else:
            break

    for i in range(4):
        if final_dirs[i] != 0:
            gears_rotate(i,final_dirs[i])

ans = 0       
for i in range(4):
    if gears[i][0] == 1:
        ans += 2**i

print(ans)
