from collections import deque
from glob import glob
from os import stat
from pprint import pprint
import sys

input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(m)]
pprint(graph)
sx, sy = -1, -1

bit_dic = {}
x_num = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == "S":
            sx, sy = i, j
        elif graph[i][j] == "X":
            bit_dic[(i, j)] = 1 << x_num
            x_num += 1

target = sum(bit_dic.values())
print(bin(target)[2:])
visited = [[[False for _ in range(n)] for _ in range(m)] for _ in range(1 << (x_num) + 1)]
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

print(x_num)
ans = int(1e9)
def bfs(sx, sy):
    global ans

    Q = deque([(sx, sy, 0, 0)])
    visited[0][sx][sy] = True

    while Q:

        x, y, state, dist = Q.popleft()
        print(x, y, bin(state)[2:], dist)
        if ans < dist: continue
        if state == target and graph[x][y] == "E":
            ans = min(dist, ans)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < m and 0 <= ny < n): continue
            if graph[nx][ny] == "#": continue
            if graph[nx][ny] == "X":
                state |= bit_dic[(nx, ny)]
            
            if visited[state][nx][ny]: continue
            # print(x_num, state, nx, ny)
            visited[state][nx][ny] = True
            Q.append((nx, ny, state,  dist + 1))

bfs(sx, sy)
print(ans)