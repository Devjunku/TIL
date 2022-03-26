from copy import deepcopy
import sys
input = sys.stdin.readline

bowl = [[] for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))

    fish = []
    for j in range(0, 8, 2):
        fish.append([data[j], data[j+1]-1])
    
    bowl[i] = fish


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0
def dfs(sx, sy, score, c_bowl):
    global answer
    score += c_bowl[sx][sy][0]
    c_bowl[sx][sy][0] = 0
    answer = max(answer, score)

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
        for i in range(8):
            nd = (fd+i) % 8
            nx, ny = fx + dx[nd], fy + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue

            if nx == sx and ny == sy:
                continue

            c_bowl[fx][fy][1] = nd
            c_bowl[fx][fy], c_bowl[nx][ny] = c_bowl[nx][ny], c_bowl[fx][fy]
            break
    
    sd = c_bowl[sx][sy][1]
    for i in range(1, 5):
        nx, ny = sx + dx[sd] * i, sy + dy[sd] * i

        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue

        if c_bowl[nx][ny][0] == 0:
            continue

        dfs(nx, ny, score, deepcopy(c_bowl))

dfs(0, 0, 0, bowl)
print(answer)