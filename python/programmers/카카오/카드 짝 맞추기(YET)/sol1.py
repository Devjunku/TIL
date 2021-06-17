from pandas import DataFrame
from itertools import permutations
from collections import deque
from copy import deepcopy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

direct = ['up', 'down', 'right', 'left']

INF = int(1e9)


def ctrl_move(x, y, INF_board, board, direct):
    board[x][y] = 0
    if direct == 'up':
        while x != 0:
            if board[x][y] == 0:
                x -= 1
            else:
                break
    elif direct == 'down':
        while x != 3:
            if board[x][y] == 0:
                x += 1
            else:
                break
    elif direct == 'right':
        while y != 3:
            if board[x][y] == 0:
                y += 1
            else:
                break
    elif direct == 'left':
        while y != 0:
            if board[x][y] == 0:
                y -= 1
            else:
                break

    return (x, y)


def bfs(x, y, INF_board, board):
    q = deque([(x, y)])
    INF_board[x][y] = 0

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and INF_board[nx][ny] == INF:
                INF_board[nx][ny] = INF_board[cx][cy] + 1
                q.append((nx, ny))
    
    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()

        for d in direct:
            nx, ny = ctrl_move(cx, cy, INF_board, board, d)
            if INF_board[nx][ny] > INF_board[cx][cy] + 1:
                INF_board[nx][ny] = INF_board[cx][cy] + 1
                q.append((nx, ny))
    
    return INF_board


def solution(board, r, c):

    target_list = set()

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
               target_list.add(board[i][j])

    targets = list(permutations(list(target_list), 3))
    

    res = INF
    for target in targets:
        board1 = deepcopy(board)
        cnt = 0
        sr, sc = r, c
        for num in target:
            INF_board = [[INF for _ in range(4)] for _ in range(4)]
            for _ in range(2):
                dist = INF
                distance = bfs(sr, sc, INF_board, board1)
                for i in range(4):
                    for j in range(4):
                        if num == board1[i][j] and distance[i][j] < dist:
                            dist = distance[i][j]
                            sr, sc = i, j
                board1[sr][sc] = 0
                cnt += dist+1
        if res > cnt:
            res = cnt

    print(res)
                

if __name__ == '__main__':
    print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
    print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))