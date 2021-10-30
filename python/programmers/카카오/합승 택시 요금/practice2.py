from sys import maxsize
from heapq import heappop, heappush

def dijkstra(s, e, n, graph):
    
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[s] = 0
    q = []
    heappush(q, (0, s))
    while q:
        dist, now = heappop(q)
        
        if dist > distance[now]:
            continue
        
        for nxt, cost in graph[now]:
            cost = dist + cost

            if distance[nxt] > cost:
                distance[nxt] = cost
                heappush(q, (cost, nxt))
                
    return distance[e]
    

def solution(n, s, a, b, fares):
    
    graph = [[] for _ in range(n+1)]
    
    for fare in fares:
        c, d, f = fare
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    res = maxsize
    for i in range(1, n+1):
        res = min(res, dijkstra(s, i, n, graph) + dijkstra(i, a, n, graph) + dijkstra(i, b, n, graph))
        
    return res

if __name__ == "__main__":
    print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
    print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
    print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))