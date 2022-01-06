# queue는 메모리 초과 남
# queue를 사용하지 않는 방법을 생각하자. 그니까 그냥 좌표 값 표기로 계산할 수 있는 방법을 찾자
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]


def bfs(x, y):

    q = deque([(x, y, 0)])

    while q:
        cx, cy, dist = q.popleft()
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    return dist + 1
                else:
                    q.append((nx, ny, dist+1))
    
    return ans

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            continue
        ans = max(ans, bfs(i, j))

print(ans)