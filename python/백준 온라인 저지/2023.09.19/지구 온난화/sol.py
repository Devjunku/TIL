import sys
from copy import deepcopy
input = sys.stdin.readline

R, C = map(int, input().split())

sea_land = []

for i in range(R):
    sea_land.append(+list(input().strip()))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def after_50_years(land, R, C):

    result = deepcopy(land)

    for i in range(R):
        for j in range(C):

            if land[i][j] == ".": continue

            num = 0
            cx, cy = i, j
            for k in range(4):
                nx, ny = cx + dx[k], cy + dy[k]
                if not (0 <= nx < R and 0 <= ny < C):
                    num += 1
                    continue
                if land[nx][ny] == ".": num += 1
            
            if num > 2:
                result[i][j] = "."

    row = []
    for i in range(R):
        if "X" in result[i]: row.append(i)
    
    result_r = list(zip(*result[::-1]))

    col = []
    for i in range(C):
        if "X" in result_r[i]: col.append(i)
    
    answer = [[] for _ in range(len(row))]

    for i in range(len(row)):
        for j in range(min(col), max(col)+1):
            answer[i].append(result[row[i]][j])

    return answer

for a in after_50_years(sea_land, R, C):
    print("".join(a))