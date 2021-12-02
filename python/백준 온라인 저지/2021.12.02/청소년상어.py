import copy

board = [[] for _ in range(4)]

# 위치 선정
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish

max_score = 0

def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    for f in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    fx, fy = x, y
                    break
        if fx == -1 and fy == -1:
            continue
        fd = board[fx][fy][1]

        for i in range(8):
            nd = (fd + i) % 8
            nx, ny = fx + dx[nd], fy + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[fx][fy][1] = nd
            board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
            break

    sd = board[sx][sy][1]
    for i in range(1, 5):
        nx, ny = sx + dx[sd]*i, sy + dy[sd]*i
        if (0 <= nx < 4 and 0 <= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)