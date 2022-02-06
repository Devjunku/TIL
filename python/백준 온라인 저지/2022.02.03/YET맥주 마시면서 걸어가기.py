from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    q, c = deque(), []

    q.append([x, y, 20])
    c.append([x, y, 20])
    
    while q:
        x, y, beer = q.popleft()
        if x == x1 and y == y1:
            print("happy")
            return
        
        for nx, ny in d:
            if [nx, ny, 20] not in c:
                if beer * 50 >= abs(x-nx) + abs(y-ny):
                    q.append([nx, ny, 20])
                    c.append([nx, ny, 20])
    print("sad")
    return


T = int(input())

for _ in range(T):
    n = int(input())
    x0, y0 = map(int, input().split())
    d = []
    for _ in range(n):
        x, y = map(int, input().split())
        d.append([x, y])
    x1, y1 = map(int, input().split())        
    d.append([x1, y1])
    bfs(x0, y0)