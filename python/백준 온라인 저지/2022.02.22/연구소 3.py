import sys
from itertools import combinations
from copy import deepcopy
from pprint import pprint
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

virus_loc = []

for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus_loc.append((i, j, 0))

virus_loc_m = combinations(virus_loc, m)

def bfs(ele, arr):

    visited = [[False for _ in range(n)] for _ in range(n)]

    for i, j, c in ele:
        arr[i][j] = 0
        visited[i][j] = True
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                arr[i][j] = "*"
            elif arr[i][j] == 1:
                arr[i][j] = "-"
    
    q = deque([])
    for e in ele:
        q.append(e)
    
    max_value = 0


    while q:
        x, y, count = q.popleft()
        max_value = max(max_value, count)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if arr[nx][ny] == 0:
                        visited[nx][ny] = True
                        arr[nx][ny] = arr[x][y] + 1
                        q.append((nx, ny, count + 1))
    
    return max_value
ans = int(1e9)
for e in virus_loc_m: 
    ans = min(ans, bfs(e, deepcopy(lab)))

print(ans)