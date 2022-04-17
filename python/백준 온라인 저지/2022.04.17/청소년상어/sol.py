from copy import deepcopy
import sys
input = sys.stdin.readline

bowl = [[] for _ in range(4)]
sx, sy = 0, 0

for i in range(4):
    data = list(map(int, input().split()))

    fish = []
    for j in range(0, 8, 2):
        fish.append([data[j], data[j+1]-1])
    
    bowl[i] = fish

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

ans = 0
def find_max_score(sx, sy, fish_bowl, score):
    global ans
    score += fish_bowl[sx][sy][0]
    fish_bowl[sx][sy][0] = 0
    ans = max(ans, score)

    for fish_number in range(1,  17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if fish_bowl[x][y][0] == fish_number:
                    fx, fy = x, y
                    break
        
        if fx == -1 and fy == -1: continue

        fd = fish_bowl[fx][fy][1]
        for i in range(8):
            nd = (fd+i) % 8
            nx, ny = fx + dx[nd], fy + dy[nd]
            
            if not (0 <= nx < 4 and 0 <= ny < 4) or nx == sx and ny == sy:
                continue

            fish_bowl[fx][fy][1] = nd
            fish_bowl[fx][fy], fish_bowl[nx][ny] = fish_bowl[nx][ny], fish_bowl[fx][fy]
            break
    
    sd = fish_bowl[sx][sy][1]
    for i in range(1, 5):
        nx, ny = sx + dx[sd] * i, sy + dy[sd] * i

        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue

        if fish_bowl[nx][ny][0] == 0:
            continue

        find_max_score(nx, ny, deepcopy(fish_bowl), score)


find_max_score(0, 0, bowl, 0)
print(ans)