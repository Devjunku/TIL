import sys
from pandas import DataFrame
sys.stdin = open('sample_input.txt')





direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(x, y, loc_n, cnt, direc_x, direc_y):
    global res
    print(DataFrame(board))
    print()
    if cnt > res:
        return

    if loc_n >= nums:
        if cnt < res:
            res = cnt
            return
    
    for i in range(4):
        nx, ny = x + direct[i][0], y + direct[i][1]
        if 0 <= nx < N and  0 <= ny < N and board[nx][ny] == 0:
            if (direc_x == 0 and direc_y == 0) or (direc_x == direct[i][0] and direc_y == direct[i][1]):
                board[nx][ny] = 1
                dfs(nx, ny, loc_n, cnt+1, direct[i][0], direct[i][1])
                board[nx][ny] = 0
    
    if loc_n+1 < nums:
        dfs(loc[loc_n+1][0], loc[loc_n+1][1] ,loc_n+1, cnt, 0, 0)
    



T = int(input())

for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    loc = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 and 0 < i < N-1 and 0 < j < N-1:
                loc.append((i, j))
    nums = len(loc)
    res = int(1e9)
    dfs(loc[0][0], loc[0][1], 0, 0, 0, 0)
    print(res)