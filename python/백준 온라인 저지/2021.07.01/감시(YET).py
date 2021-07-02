from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(cnt):
    global ans, temp_a
    if cnt == len(cctv):
        temp_a = deepcopy(a)
        c = 0
        for i in range(len(cctv)):
            x, y = cctv[i]
            if a[x][y] == 1:
                c += move(x, y, dir[i])
            elif a[x][y] == 2:
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 2) % 4)
            elif a[x][y] == 3:
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 1) % 4)
            else:
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 1) % 4)
                c += move(x, y, (dir[i] + 2) % 4)
        ans = min(ans, area - c)
        return

    for i in range(4):
        dir.append(i)
        dfs(cnt + 1)
        dir.pop()


def move(x, y, d):
    cnt = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if not 0 <= nx < n or not 0 <= ny < m or temp_a[nx][ny] == 6:
            return cnt
        if 0 < temp_a[nx][ny] < 6 or temp_a[nx][ny] == -1:
            x, y = nx, ny
            continue
        temp_a[nx][ny] = -1
        cnt += 1
        x, y = nx, ny


n, m = map(int, input().split())
area = n * m
a, cctv, cctv5 = [], [], []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    for j in range(m):
        if 0 < a[i][j] < 5:
            cctv.append([i, j])
            area -= 1
        elif a[i][j] == 5:
            cctv5.append([i, j])
            area -= 1
        elif a[i][j] == 6:
            area -= 1

for i in range(len(cctv5)):
    x, y = cctv5[i]
    for i in range(4):
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if not 0 <= nx < n or not 0 <= ny < m or a[nx][ny] == 6:
                break
            if 0 < a[nx][ny] < 6 or a[nx][ny] == -1:
                continue
            a[nx][ny] = -1
            area -= 1

dir = deque()
ans = area
dfs(0)
print(ans)