from collections import deque

def safe(y, x):
    global n, m
    if y >= n or y < 0 or x >= m or x < 0:
        return False
    if arr[y][x] == 1:
        return False
    return True

def BFS(y, x):
    global arr
    queue = deque()
    queue.append((y, x))
    cnt = 0
    while queue:
        y, x = queue.popleft()
        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            if not safe(ny, nx):
                continue
            else: 
                if arr[ny][nx] == -1:
                    cnt += 1
                else:
                    queue.append((ny, nx))
    return cnt

def solution(m, n , puddles):
    
    dy = [1, 0]
    dx = [0, 1]
    
    m = m
    n = n

    arr = [[0] * m for _ in range(n)]
    
    for i, j in puddles:
        arr[i-1][j-1] = 1

    arr[n-1][m-1] = -1

    return BFS(0, 0)



if __name__ == '__main__':
    print(solution(m = 4, n = 3, puddles = [[2,2]]))