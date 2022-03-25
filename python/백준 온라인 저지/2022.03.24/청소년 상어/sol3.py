import sys
from copy import deepcopy
input = sys.stdin.readline

bowl = [[]for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    fish_info = []
    for j in range(0, 8, 2):
        fish_info.append([data[j], data[j+1]-1])

    bowl[i] = fish_info

max_score = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(sx, sy, score, c_bowl):
    global max_score
    score += c_bowl[sx][sy][0]
    c_bowl[sx][sy][0] = 0
    max_score = max(max_score, score)

    # 물고리 움직이기

    # TODO: Step 1 → 물고리 찾기
    for fish in range(1, 17):
        fx, fy = -1, -1

        for x in range(4):
            for y in range(4):
                if c_bowl[x][y][0] == fish:
                    fx, fy = x, y
                    break
        if fx == -1 and fy == -1:
            continue

        fd = c_bowl[fx][fy][1]

        # TODO: Step 2 → 방향 설정하기 
        for i in range(8):
            nd = (fd+i) % 8
            nx, ny = fx + dx[nd], fy + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue

            c_bowl[fx][fy][1] = nd
            c_bowl[fx][fy], c_bowl[nx][ny] = c_bowl[nx][ny], c_bowl[fx][fy]
            break

    # TODO: Step3 → 상어 이동시키기
    sd = c_bowl[sx][sy][1]
    for i in range(1, 5):
        nx, ny = sx + dx[sd]*i, sy + dy[sd]*i

        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue

        if c_bowl[nx][ny][0] <= 0:
            continue

        dfs(nx, ny, score, deepcopy(c_bowl))
    
dfs(0, 0, 0, bowl)
print(max_score)