from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
board = [[0 for _ in range(c)] for _ in range(r)]
check_point = []
warm_machine_loc = []
wall = set()

choco_num = 0

bound_point = []

for i in range(r):
    for j in range(c):
        if i == 0:
            bound_point.append((i, j))
        elif i == r-1:
            bound_point.append((i, j))
        elif j == 0:
            bound_point.append((i, j))
        elif j == c-1:
            bound_point.append((i, j))

warm_machine_direction = [
    [
        [(-1, 0), (0, 1)],
        [(0, 1)],
        [(1, 0), (0, 1)]
    ],
    [
        [(-1, 0), (0, -1)],
        [(0, -1)],
        [(1, 0), (0, -1)]
    ],
    [
        [(0, -1), (-1, 0)],
        [(-1, 0)],
        [(0, 1), (-1, 0)]
    ],
    [
        [(0, -1), (1, 0)],
        [(1, 0)],
        [(0, 1), (1, 0)]
    ]
]

for i in range(r):
    data = list(map(int, input().split()))
    for j in range(c):
        if data[j] in [1, 2, 3, 4]:
            warm_machine_loc.append((i, j, data[j]-1))
        elif data[j] == 5:
            check_point.append((i, j))

w = int(input())
for _ in range(w):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        wall.add((x, y, x-1, y))
        wall.add((x-1, y, x, y))
    else:
        wall.add((x, y, x, y+1))
        wall.add((x, y+1, x, y))

def confirm_k_up():

    for x, y in check_point:
        if board[x][y] < k:
            return True
    
    return False

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def update_c():
    global board
    new_board = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            plus = 0
            mius = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if not (0 <= nx < r and 0 <= ny < c): continue
                if (i, j, nx, ny) in wall or (nx, ny, i, j) in wall: continue
                if board[i][j] > board[nx][ny]:
                    mius += abs(board[i][j]-board[nx][ny]) // 4
                elif board[i][j] < board[nx][ny]:
                    plus += abs(board[i][j]-board[nx][ny]) // 4

            new_board[i][j] = board[i][j] + plus - mius
    
    board = deepcopy(new_board)


def spread_warm(q, d, v):
    nxt_q = deque([])
    while q:
        sx, sy = q.popleft()
        for route in warm_machine_direction[d]:
            x, y = sx, sy
            for d_x, d_y in route:
                nx, ny = x + d_x, y + d_y
                if not (0 <= nx < r and 0 <= ny < c): break
                if (x, y, nx, ny) in wall or (nx, ny, x, y) in wall: break
                x, y = nx, ny
            else:
                if visited[x][y]: continue
                visited[x][y] = True
                if v > 0:
                    board[x][y] += v
                    nxt_q.append((x, y))

    return nxt_q

while confirm_k_up():

    if choco_num > 100:
        print(101)
        exit()

    # TODO 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
    for x, y, d in warm_machine_loc:
        nx, ny = x + dx[d], y + dy[d]
        v = 5
        board[nx][ny] += v
        v -= 1
        q = deque([(nx, ny)])
        visited = [[False for _ in range(c)] for _ in range(r)]
        while q:
            q = spread_warm(q, d, v)
            v -= 1
    
    # TODO 온도가 조절됨
    update_c()

    # TODO 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    for x, y in bound_point:
        if board[x][y] >= 1:
            board[x][y] -= 1

    choco_num += 1

print(choco_num)