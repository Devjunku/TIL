import sys
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

def bfs(sx, sy, score, c_bowl):
    global max_score
    score += bowl[sx][sy]
    bowl[sx][sy] = 0
    max_score = max(max_score, score)

    # 물고리 움직이기

    # TODO: Step 1 → 물고리 찾기
    for fish in range(1, 17):
        fx, fy = -1, -1

        for i in range(4):
            for j in range(4):
                if c_bowl[i][j] == fish:
                    fx, fy = i, j
                    break
        
        if fx == -1 and fy == -1:
            continue







