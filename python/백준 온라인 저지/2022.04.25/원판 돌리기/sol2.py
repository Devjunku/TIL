from collections import deque
import sys

input = sys.stdin.readline

n, m, t = map(int, input().split())

circle = []
for _ in range(n):
    circle.append(deque(list(map(int, input().split()))))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def find_equal_number(i, j):
    global exist

    q = deque([(i, j)])

    delete_list = [(i, j)]
    while q:
        x, y = q.popleft()
        for n_d in range(4):
            nx, ny = x + dx[n_d], (y + dy[n_d]) % m if (y + dy[n_d]) % m >= 0 else m - 1

            if not (0 <= nx < n): continue
            if visited[nx][ny]: continue
            if circle[nx][ny] == 0: continue
            if circle[nx][ny] != circle[i][j]: continue

            visited[nx][ny] = True
            q.append((nx, ny))
            delete_list.append((nx, ny))

    if len(delete_list) > 1:
        exist = False
        for x, y in delete_list:
            circle[x][y] = 0


for _ in range(t):
    x, d, k = map(int, input().split())

    start_idx = x - 1

    while start_idx < n:
        if d == 0:
            circle[start_idx].rotate(k)
        else:
            circle[start_idx].rotate(-k)
        start_idx += x

    exist = True
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and circle[i][j] != 0:
                visited[i][j] = True
                find_equal_number(i, j)

    if exist:
        sum_number = 0
        not_zero_number = 0
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    sum_number += circle[i][j]
                    not_zero_number += 1
        
        if not_zero_number:
            mean = sum_number / not_zero_number

            for i in range(n):
                for j in range(m):
                    if circle[i][j] == 0: continue
                    if circle[i][j] > mean:
                        circle[i][j] -= 1
                    elif circle[i][j] < mean:
                        circle[i][j] += 1

ans = 0
for i in range(n):
    ans += sum(circle[i])
print(ans)