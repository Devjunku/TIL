import sys

sys.stdin = open('input.txt')

from collections import deque

def safe(x, y):
    if x >= N or x < 0 or y >= N or y < 0:
        return False
    return True


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [ list(map(int, list(input()))) for _ in range(N)]
    min_list = [[-1 for _ in range(N)] for _ in range(N)]
    min_list[0][0] = 0
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<N and 0<=y<N):
                continue
            if min_list[nx][ny] == -1:
                min_list[nx][ny] = min_list[nx][ny] + arr[nx][ny]
                queue.append((nx,ny))
            elif min_list[nx][ny] > min_list[nx][ny] + arr[nx][ny]:
                min_list[nx][ny] = min_list[nx][ny] + arr[nx][ny]
                queue.append((nx,ny))    
    print(min_list[-1][-1])





