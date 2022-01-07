
# pypy3 통과
# python 3 미통과
from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

virus_point = []
for i in range(n):
    for j in range(m):
        if room[i][j] == 2:
            virus_point.append((i, j))

cnt =  0

def dfs(room, num):
    global cnt, n, m
    
    if num == 3:
        c = spread(room) # 안전영역을 구하기
        cnt = max(cnt, c)
        return

    for i in range(n):
        for j in range(m):

            if room[i][j] == 0:
                room[i][j] = 1
                dfs(deepcopy(room), num+1)
                room[i][j] = 0

def spread(room):
    global virus_point, n, m

    res = 0
    for vp in virus_point:
        x, y = vp
        q = deque([])
        q.append((x, y))
        res = 0

        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if room[nx][ny] == 0:
                        room[nx][ny] = 2
                        q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if room[i][j] == 0:
                res += 1

    return res

dfs(room, 0)
print(cnt)