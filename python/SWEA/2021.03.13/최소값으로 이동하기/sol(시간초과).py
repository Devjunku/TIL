import sys
from pandas import DataFrame
sys.stdin = open('sample_input.txt')

# 1 델타이동
# 이거 y를 기준으로 놔야함

dy = [1, -1, 0, 0, 1, -1] # 방향
dx = [0, 0, -1, 1, 1, -1] # 방향

def safe(x, y):
    global arr_test
    if y >= W or y < 0 or x >= H or x < 0:
        return False
    else:
        if arr_test[x][y] == 1:
            False
        else:
            return True


def bfs(start, end):
    global arr_test, cnt
    ey, ex = end
    queue = [start]
    while queue:
        while queue:
            stack = []
            y, x = queue.pop(0)
            arr_test[x][y] = 1
            for i in range(6):
                ny, nx = y + dy[i], x + dx[i]
                if safe(nx, ny):
                    arr_test[nx][ny] = 1
                    stack.append([ny, nx])
                if arr_test[ex][ey] == 1:
                    cnt += 1
                    return cnt
        if len(queue) == 0:
            cnt += 1
        queue.extend(stack)
        if arr_test[ex][ey] == 1:
            break

                  
T = int(input())

for t in range(1, T+1):
    W, H, N = map(int, input().split())
    arr = [[0 for _ in range(W)] for _ in range(H)]
    points = []
    cnt = 0

    for _ in range(N):
        y, x = map(int, input().split())
        points.append([y-1, x-1])

    for i in range(len(points)-1):
        arr_test = arr.copy()
        bfs(points[i], points[i+1])
    print('#{} {}'.format(t, cnt))
    


