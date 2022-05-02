from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
board = [[0 for _ in range(c)] for _ in range(r)]

warm_machine = []
check_point = []
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

for i in range(r):
    data = list(map(int, input().split()))
    for j in range(c):
        if data[j] in [1, 2, 3, 4]:
            warm_machine.append((i, j, data[j]-1))
        elif data[j] == 5:
            check_point.append((i, j))

dx = [0, 0, -1, 1]
dy = [1,  -1, 0, 0]

warm_d = [
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


w = int(input())
wall = set()
for _ in range(w):
    x, y, t = map(int, input().split())
    if t == 0:
        wall.add((x-1, y-1, x-2, y-1))
        wall.add((x-2, y-1, x-1, y-1))
    elif t == 1:
        wall.add((x-1, y-1, x-1, y))
        wall.add((x-1, y, x-1, y-1))

choco = 0

"""
1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
2. 온도가 조절됨
3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
4. 초콜릿을 하나 먹는다.
5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
"""

def confirm():
    for x, y in check_point:
        if board[x][y] < k:
            return True
    
    return False


def spread_wind(visited, d, q, v):

    result = deque([])
    while q:
        i, j = q.popleft()
        for direct in warm_d[d]:
            flag = True
            x, y = i, j
            for d_x, d_y in direct:
                nx, ny = x + d_x, y + d_y
                if not (0 <= nx < r and 0 <= ny < c): 
                    flag = False
                    break
                if (nx, ny, x, y) in wall or (x, y, nx, ny) in wall:
                    flag = False
                    break
                if visited[nx][ny]:
                    flag = False
                    break
                x, y = nx, ny
            if flag:
                if v > 0:
                    visited[nx][ny] = True
                    board[nx][ny] += v
                    result.append((nx, ny))
    
    return result


def plus_mius_c():
    global board
    new_board = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            x, y = i, j
            plus = 0
            mius = 0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if not (0 <= nx < r and 0 <= ny < c): continue
                if (nx, ny, x, y) in wall or (x, y, nx, ny) in wall: continue

                if board[nx][ny] > board[x][y]:
                    plus += abs(board[nx][ny] - board[x][y])//4
                elif board[nx][ny] < board[x][y]:
                    mius += abs(board[nx][ny] - board[x][y])//4
            new_board[i][j] = board[i][j] + plus - mius
    board = deepcopy(new_board)



while confirm():
    # TODO 바람 나옴
    for x, y, d in warm_machine:
        v = 5
        nx, ny = x + dx[d], y + dy[d]
        board[nx][ny] += v
        q = deque([(nx, ny)])
        v -= 1
        while q:
            visited = [[False for _ in range(c)] for _ in range(r)]
            if v > 0:
                q = spread_wind(visited, d, q, v)
            else:
                break
            v -= 1
    # TODO 온도가 조절됨
    plus_mius_c()

    # TODO 바깥쪽 온도 -1씩 감소
    for x, y in bound_point:
        if board[x][y] > 0:
            board[x][y] -= 1
    

    choco += 1

    if choco > 100:
        break

print(choco)