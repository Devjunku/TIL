from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline

board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
b = [[[0]*5 for _ in range(5)] for _ in range(5)]
result = sys.maxsize

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def rotate(b):
    tmp = [[0]*5 for _ in range(5)]
    for i in range(len(b)):
        for j in range(len(b[0])):
            tmp[j][4-i] = b[i][j]

    return tmp

def bfs(b):
    global result
    q = deque()
    dist = [[[0, 0, 0, 0, 0] for _ in range(5)] for _ in range(5)]
    q.append((0,0,0))

    while q:
        ch, cy, cx = q.popleft()
        if (ch, cy, cx) == (4, 4, 4):
            result = min(result, dist[4][4][4])
            if result == 12:
                print(result)
                exit()
            return
        
        for i in range(6):
            nh, ny, nx = ch + dz[i], cy + dy[i], cx + dx[i]

            if not (0 <= nx < 5 and 0 <= ny < 5 and 0 <= nh < 5):
                continue
            elif b[nh][ny][nx] == 0 or dist[nh][ny][nx] != 0:
                continue
            
            q.append((nh, ny, nx))
            dist[nh][ny][nx] = dist[ch][cy][cx] + 1

def dfs(d):
    global b
    if d == 5:
        if b[4][4][4]:
            bfs(b)
        return
    
    for i in range(4):
        if b[0][0][0]:
            dfs(d + 1)
        b[d] = rotate(b[d])

def solve():
    for d in permutations([0, 1, 2, 3, 4]):
        for i in range(5):
            b[d[i]] = board[i]
        dfs(0)


solve()

if result == sys.maxsize:
    result = -1
print(result)