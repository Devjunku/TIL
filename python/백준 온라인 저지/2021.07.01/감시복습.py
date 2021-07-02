from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

def dfs(n):
    global ans, c_board
    if n == len(cctv):
        c_board = deepcopy(board)
        c = 0 
        for i in range(len(cctv)):
            x, y = cctv[i]
            if board[x][y] == 1:
                c += move(x, y, queue[i])
            elif board[x][y] == 2:
                c += move(x, y, queue[i])
                c += move(x, y, (queue[i] + 2) % 4)
            elif board[x][y] == 3:
                c += move(x, y, queue[i])
                c += move(x, y, (queue[i] + 1) % 4)
            elif board[x][y] == 4:
                c += move(x, y, queue[i])
                c += move(x, y, (queue[i] + 1) % 4)
                c += move(x, y, (queue[i] + 2) % 4)
            
        ans = min(ans, area - c)
        return

    for i in range(4):
        queue.append(i)
        dfs(n+1)
        queue.pop()


def move(x, y, d):
    cnt = 0

    while True:
        x += dx[d]
        y += dy[d]
        if  not (0 <= x < N and 0 <= y < M):
            return cnt
        
        if c_board[x][y] == 6:
            return cnt

        if c_board[x][y] == -1 or 0 < c_board[x][y] < 6:
            continue

        c_board[x][y] = -1
        cnt += 1


N, M = map(int, input().split())

area = N * M
board = []
cctv = []
cctv5 = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        if row[j] == 6:
            area -= 1
        elif row[j] == 5:
            cctv5.append((i, j))
            area -= 1
        elif 0 < row[j] < 5:
            cctv.append((i, j))
            area -= 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(len(cctv5)):
    x, y = cctv5[i]
    for j in range(4):
        while True:
            x += dx[j]
            y += dy[j]
            if  not (0 <= x < N and 0 <= y < M):
                break
            
            if board[x][y] == 6:
                break

            if 0 < board[x][y] < 6 or board[x][y] == -1:
                continue

            board[x][y] = -1
            area -= 1

queue = deque()
ans = area
dfs(0)
print(ans)
