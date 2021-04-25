from heapq import heappush, heappop

INF = int(1e9)
graph = [[]]


def edge_info(n, fares):
    global graph
    
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        s, e, w = fare[0], fare[1], fare[2]
        graph[s].append((e, w))
        graph[e].append((s, w))

        
def dijkstra(s, e):
    global graph
    
    num = len(graph)
    distance = [INF for i in range(num)]
    distance[s] = 0
    
    q = []
    heappush(q, (0, s))
    
    while q:
        
        dist, now = heappop(q)
        
        if distance[now] < dist:
            continue
            
        for node, cost in graph[now]:
            print(node, cost)
            cost += dist
            
            if distance[node] > cost:
                distance[node] = cost
                heappush(q, (node, cost))
                
    return distance[e]
    

def solution(n, s, a, b, fares):
    
    edge_info(n, fares)
    res_cost = INF
    
    for i in range(1, n+1):
        res_cost = min(res_cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return res_cost


if __name__ == '__main__':
    print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
    print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
    print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))