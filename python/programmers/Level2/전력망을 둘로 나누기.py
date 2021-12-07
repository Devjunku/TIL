import sys
from collections import deque

def bfs(s, graph, visited):

    q = deque()
    q.append(s)
    num = 1
    while q:
        node = q.popleft()
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                num += 1
                q.append(v)
    return num

def solution(n, wires):

    graph = [[] for _ in range(n+1)]

    # 양방향이기 때문에
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    answer = sys.maxsize
    for s, e in wires:
        visited = [False for _ in range(n+1)]
        visited[s] = True
        visited[e] = True
        num = bfs(s, graph, visited)

        min_v = min(num, n-num)
        max_v = n-min_v

        if answer > abs(max_v - min_v):
            answer = abs(max_v - min_v)

    return answer

if __name__ == "__main__":
    print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
    print(solution(4,[[1,2],[2,3],[3,4]]))
    print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))