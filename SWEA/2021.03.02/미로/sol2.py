import sys

sys.stdin = open('sample_input.txt')

dy = [-1, 1, 0, 0] # 방향설정
dx = [0, 0, -1, 1]

def start_end(maze):
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                return y, x


def safe(y, x):
    if 0 <= y < N and 0 <= x < N and (maze[y][x] == 0 or maze[y][x] == 3):
        return True
    else:
        return False


def dfs(y, x):
    global res

    if maze[y][x] == 3:
        res = 1
        return

    visited.append((y, x))
    for k in range(4):
        n_x = x + dx[k]
        n_y = y + dy[k]
        if safe(n_y, n_x) and (n_y, n_x) not in visited:
            dfs(n_y, n_x)


T = int(input())
for t in range(1, T+1):
    N = int(input())

    maze = [] # 데이터 받기
    for _ in range(N):
        maze.append(list(map(int, list(input()))))
    # print(maze)

    y, x = start_end(maze)

    visited = []
    res = 0
    dfs(y, x)
    print(res)