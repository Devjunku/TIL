"""
청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다.
상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다.

물고기는 번호가 작은 물고기부터 순서대로 이동한다.
물고기는 한 칸을 이동할 수 있고,
이동할 수 있는 칸: 빈 칸, 다른 물고기가 있는 칸
이동할 수 없는 칸: 상어가 있거나, 공간의 경계를 넘는 칸이다.
각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전
만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다.
그 외의 경우에는 그 칸으로 이동을 한다.
물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꿈

이후 상어가 이동

상어는 방향에 있는 칸으로 이동할 수 있는데
한 번에 여러 개의 칸을 이동할 수 있다.
상어가 물고기가 있는 칸으로 이동했다면,
그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.
이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
물고기가 없는 칸으로는 이동할 수 없다.
상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다.
상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.

↑, ↖, ←, ↙, ↓, ↘, →, ↗
"""

from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

bowl = [[] for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))

    fish = []
    for j in range(0, 8, 2):
        fish.append([data[j], data[j+1]-1])

    bowl[i] = fish

answer = 0
def solution(sx, sy, eating_score, c_bowl):
    global answer

    # TODO 1. 상어가 물고기를 먹음
    # eating_score update
    eating_score += c_bowl[sx][sy][0]
    # shark_d 상어 방향 설정
    c_bowl[sx][sy][0] = 0

    # answer 업뎃
    answer = max(answer, eating_score)

    # TODO 2. 작은 물고기부터 순서대로 이동
    
    # 작은 물고기부터 찾기
    for fish_number in range(1, 17):
        fish_x, fish_y = -1, -1
        for i in range(4):
            for j in range(4):
                if c_bowl[i][j][0] == fish_number:
                    fish_x, fish_y = i, j
                    break

            if fish_x != -1 and fish_y != -1:
                break

        # 물고기가 없는 경우 continue
        if fish_x == -1 and fish_y == -1: continue

        # 이동할 수 있는 칸: 빈 칸, 다른 물고기가 있는 칸 -> 둘 모두 스왑해야함.
        # 이동할 수 없는 칸: 상어가 있거나, 공간의 경계를 넘는 칸이다.
        cd = c_bowl[fish_x][fish_y][1]
        for i in range(8):
            nd = (cd+i) % 8
            nx, ny = fish_x + dx[nd], fish_y + dy[nd]

            # 공간의 경계를 넘는 칸 OR 상어가 있는 경우
            if not (0 <= nx < 4 and 0 <= ny < 4) or nx == sx and ny == sy:
                continue
            
            # 이동할 수 있는 경우
            c_bowl[fish_x][fish_y][1] = nd
            c_bowl[fish_x][fish_y], c_bowl[nx][ny] = c_bowl[nx][ny], c_bowl[fish_x][fish_y]
            break
    
    # pprint(c_bowl)

    # TODO 3. 상어 이동
    # 상어가 이동할 수 있는 경우: 상어가 바라는 방향에 물고기가 있는 경우
    shark_d = c_bowl[sx][sy][1]
    shark_current_x, shark_current_y = sx, sy
    for _ in range(4):
        shark_current_x += dx[shark_d]
        shark_current_y += dy[shark_d]
        
        # 경계X
        if not (0 <= shark_current_x < 4 and 0 <= shark_current_y < 4): break
        
        # 물고기 있는지 검사
        if c_bowl[shark_current_x][shark_current_y][0] == 0: continue

        solution(shark_current_x, shark_current_y, eating_score, deepcopy(c_bowl))
        

solution(0, 0, 0, deepcopy(bowl))
print(answer)