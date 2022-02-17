import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [False for _ in range(F+1)]

def bfs(now):
    q = deque([])
    q.append((now, 0))
    while q:
        stair, count = q.popleft()
        
        if stair == G:
            return count

        if stair + U <= F:
            if not visited[stair + U]:
                visited[stair + U] = True
                q.append((stair + U, count + 1))
        if 1 <= stair - D:
            if not visited[stair - D]:
                visited[stair - D] = True
                q.append((stair - D, count + 1))

    return "use the stairs"     

print(bfs(S))