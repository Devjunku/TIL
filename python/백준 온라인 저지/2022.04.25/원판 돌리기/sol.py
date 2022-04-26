from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

circle_q = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    circle_q.append(deque(list(map(int, input().split()))))

def bfs(i, j):
    global toggle

    q = deque([(i, j)])
    visited[i][j] = True
    delete_list = [(i, j)]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], (y + dy[k]) % n

            if not (0 <= nx < n): continue
            if circle_q[nx][ny] == 0: continue
            if circle_q[nx][ny] != circle_q[i][j]: continue
            if visited[nx][ny]: continue
            circle_q[nx][ny] == circle_q[i][j]
            visited[nx][ny] = True
            delete_list.append((nx, ny))
    print(delete_list)
    if len(delete_list) > 1:
        toggle = False
        for x, y in delete_list:
            circle_q[x][y] = 0


for _ in range(t):
    x, d, k = map(int, input().split())
    print(x, d, k)

    s = x - 1
    # TODO 1. 원판을 회전시킨다.
    
    while s < n:
        if d == 0:
            circle_q[s].rotate(k)
        else:
            circle_q[s].rotate(-k)
        s += x
    
    pprint(circle_q)
    # pprint(circle_q)
    # TODO 2. 인접한 칸 중에서 같은 수는 전부 지운다.
    # x는 범위가 넘어가면 안 되고 y는 됨
    visited = [[False for _ in range(n)] for _ in range(n+1)]
    toggle = True
    for i in range(n):
        for j in range(n):
            if circle_q[i][j] == 0: continue
            if not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)

    pprint(circle_q)
    if toggle:
        mean = 0
        not_zero = 0
        for i in range(n):
            mean += sum(circle_q[i])
            for j in range(n):
                if circle_q[i][j] != 0:
                    not_zero +=1
        if not_zero:
            mean /= not_zero
            print(mean)
            for i in range(n):
                for j in range(n):
                    if circle_q[i][j] == 0: continue
                    if circle_q[i][j] < mean: circle_q[i][j] += 1
                    elif circle_q[i][j] > mean: circle_q[i][j] -= 1
        pprint(circle_q)
    
pprint(circle_q)  
ans = 0
for i in range(n):
    ans += sum(circle_q[i])

print(ans)
    

