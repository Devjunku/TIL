from copy import deepcopy
import sys

from numpy import c_
input = sys.stdin.readline

bowl = [[] for _ in range(4)]

for i in range(4):
    fish_info = list(map(int, input().split()))
    data = []
    for j in range(0, 8, 2):
        data.append([fish_info[j], fish_info[j+1]-1])
    bowl[i] = data

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0
def eat_fish_max(sx, sy, score, c_bowl):
    global answer

    # TODO Step 0 → 상어가 물고기 먹기
    score += c_bowl[sx][sy][0]
    c_bowl[sx][sy][0] = 0
    answer = max(answer, score)

    # TODO Step 1 → 물고기 움직이기
    for fish in range(1, 17):
        fx, fy = -1, -1

        # TODO Step 2 → 물고기 번호가 존재하는지 확인
        for i in range(4):
            for j in range(4):
                if c_bowl[i][j][0] == fish:
                    fx, fy = i, j
                    break

        # TODO Step 3 → 물고기가 없으면 다음으로 넘어감
        if fx == -1 and fy == -1:
            continue
        
        # TODO Step 4 → 물고기를 찾았으면 해당 물고기의 방향을 저장
        fd = c_bowl[fx][fy][1]

        # TODO Step 5 → 45도씩 회전하면서 갈 수 있는지 확인
        # 1. 범위를 벗어나면 못감
        # 2. 상어가 있는 곳이면 못감 (상어는 sx, sy임)
        # print("여기!")
        for i in range(8):
            nd = (fd+i) % 8
            nx, ny = fx + dx[nd], fy + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue

            if nx == sx and ny == sy:
                continue
            
            # TODO Step 6 → 방향을 바꿔주고 서로의 정보를 스왑!
            c_bowl[fx][fy][1] = nd
            c_bowl[fx][fy], c_bowl[nx][ny] = c_bowl[nx][ny], c_bowl[fx][fy]
            break
    
    # TODO Step 7 → 상어 이동!
    sd = c_bowl[sx][sy][1]
    for i in range(1, 5):
        nx, ny = sx + dx[sd] * i, sy + dy[sd] * i

        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue

        if c_bowl[nx][ny][0] == 0:
            continue
        
        eat_fish_max(nx, ny, score, deepcopy(c_bowl))


eat_fish_max(0, 0, 0, bowl)
print(answer)