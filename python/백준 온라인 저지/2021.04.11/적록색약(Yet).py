from collections import deque
N = int(input())
arr = [list(input()) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def p_col_bfs(arr):
    q = deque()
    for i in range(N):
        for j in range(N):
            if not arr[i][j].isdigit():
                arr[i][j]
                q.append((x, y)):
                while q:
                    cx, cy = q.popleft()        
