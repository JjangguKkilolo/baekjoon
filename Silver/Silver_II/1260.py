import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

DFS_list = deque([V])

BFS_list = [V]

def DFS(index, current_node):
    min_dfs = int(1e9)
    
    if index == N:
        return
    for i in range(M):
        if (current_node == tree[i][0]) and (tree[i][1] not in DFS_list):
            min_dfs = min(min_dfs, tree[i][1])
        if (current_node == tree[i][1]) and (tree[i][0] not in DFS_list):
            min_dfs = min(min_dfs, tree[i][0])

    DFS_list.append(min_dfs)
    DFS(index+1, min_dfs)

def BFS(current_node):
    min_bfs = int(1e9)
    
    

DFS(1,V)
print(*DFS_list)
            
