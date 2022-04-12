import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
v = [[0] * c for _ in range(r)]
arr = []
sx, sy = 0, 0
zx, zy = 0, 0
fx, fy = 0, 0
checklist = []

for i in range(r):
    data = list(input().strip())
    arr.append(data)
    for j in range(c):
        if data[j] == "M":
            sx, sy = i, j
        elif data[j] == "Z":
            zx, zy = i, j

pipe = ["|", "-", "+", "1", "2", "3", "4"]

def direction(s):
    if s == "|":
        return [1, 3]
    elif s == "-":
        return [0, 2]
    elif s == "+" or s == "M" or s == "Z":
        return [0, 1, 2, 3]
    elif s == "1":
        return [0, 1]
    elif s == "2":
        return [0, 3]
    elif s == "3":
        return [2, 3]
    elif s == "4":
        return [1, 2]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, dirc):
    global fx, fy

    q = deque([])
    q.append((x, y, dirc))
    v[x][y] = 1
    
    while q:
        x, y, dirc = q.popleft()
        for d in dirc:
            nx, ny = x + dx[d], y + dy[d]

            if not (0 <= nx < r and 0 <= ny < c and not v[nx][ny]):
                continue

            if arr[nx][ny] != ".":
                v[nx][ny] = 1
                ndirc = direction(arr[nx][ny])
                q.append((nx, ny, ndirc))
            else:
                if arr[x][y] == "M" or arr[x][y] == "Z":
                    continue
                if not fx and not fy:
                    fx, fy = nx + 1, ny + 1
                nd = (d+2) % 4
                if nd not in checklist:
                    checklist.append(nd)

bfs(sx, sy, [0, 1, 2, 3])
bfs(zx, zy, [0, 1, 2, 3])

for i in range(r):
    for j in range(c):
        if arr[i][j] != "." and not v[i][j]:
            bfs(i, j, direction(arr[i][j]))

checklist.sort()

if len(checklist) == 4:
    print(fx, fy, "+")
else:
    for p in pipe:
        if checklist == direction(p):
            print(fx, fy, p)