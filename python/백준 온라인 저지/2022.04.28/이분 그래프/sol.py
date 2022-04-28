import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)
T = int(input())

def is_recycle(start, group):
    global answer

    if answer: return

    visited[start] = group

    for nxt in graph[start]:
        if not visited[nxt]:
            is_recycle(nxt, -group)
        elif visited[nxt] == visited[start]:
            answer = True
            return

for _ in range(1, T+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    answer = False
    visited = [0 for _ in range(v+1)]
    for _ in range(e):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    for i in range(1, v+1):
        if not visited[i]:
            is_recycle(i, 1)
            if answer: break
    print("NO") if answer else print("YES")
        