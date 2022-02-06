# python3 -> 시간 초과
# pypy -> 통과

from copy import deepcopy
from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
now_ice = [list(map(int, input().split())) for _ in range(n)]
nxt_ice = deepcopy(now_ice)


# ice의 위치를 알려주는 함수
def comfirm_ice(arr):
    is_ice = []
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                is_ice.append((i, j))
    
    return is_ice


# melting 진행하는 함수
def melting(now_field, nxt_field):

    ice_field = comfirm_ice(now_field)
    for x, y in ice_field:
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if now_field[nx][ny] == 0:
                    cnt += 1
            
        nxt_field[x][y] = max(now_field[x][y] - cnt, 0)

    return nxt_field


def bfs(x, y):
    global visited, now_ice
    visited[x][y] = True

    q = deque([(x, y)])

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and now_ice[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
t = 0
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(m):
            if now_ice[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                count += 1
    
    if count >= 2:
        print(t)
        break

    if count == 0:
        print(0)
        break

    now_ice = melting(now_ice, nxt_ice)
    nxt_ice = deepcopy(now_ice)
    t += 1