import sys

sys.stdin = open('input.txt')

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def start_point(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j

def solution(y, x):
    queue = [(y, x)]
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 16 or nx < 0 or ny >= 16:
                continue
            if maze[ny][nx] == 1:
                continue
            if maze[ny][nx] == 0:
                maze[ny][nx] = maze[y][x] + 2
                queue.append((ny, nx))
            if maze[ny][nx] == 3:
                return 1
    return 0


for _ in range(1, 11):
    t = int(input())

    maze = [ list(map(int, input())) for _ in range(16)]
    # print(maze)

    y, x = start_point(maze)
    print('#{} {}'.format(t, solution(y, x)))
