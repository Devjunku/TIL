import sys
from pandas import DataFrame

# from collections import deque
sys.stdin = open('sample_input.txt')

# 방향 설정
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# 갈 수 있는지
def NOTsafe(y, x):
    if 0 > y or y >= N or 0 > x or x >= N:
        return True
    else:
        return False


# BFS 시작
def BFS(y, x):
    queue = []
    queue.append([y, x])
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if NOTsafe(ny, nx):
                continue
            if maze[ny][nx] == 1:
                continue
            if maze[ny][nx] == 0 or maze[ny][nx] == 3:
                maze[ny][nx] = maze[y][x] + 1
                queue.append([ny, nx])

    return maze[ey][ex]-3


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    maze1 = [[0] * N for _ in range(N)]
    # print(maze)
    # print(maze1)

    # 시작과 끝
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                y, x = i, j
            if maze[i][j] == 3:
                ey, ex = i, j

    print('#{} {}'.format(t, BFS(y, x)))
