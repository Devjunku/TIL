import sys

graph1 = []
graph2 = []
res = sys.maxsize

def dfs(start, end, traps, graph, visited, total):
    global graph1, graph2, res

    visited[start] = 1

    if start == end:
        if res > total:
            res = total
        return
    
    if res < total:
        return

    for node in graph[start]:
        nxt, cost = node
        if nxt in traps:
            if visited[nxt] < 2:
                if graph == graph1:
                    dfs(nxt, end, traps, graph2, visited, total+cost)
                else:
                    dfs(nxt, end, traps, graph1, visited, total+cost)
        else:
            if not visited[nxt]:
                dfs(nxt, end, traps, graph, visited, total+cost)
        visited[nxt] = 0


def solution(n, start, end, roads, traps):
    global graph1, graph2

    visited = [0] * (n+1)
    graph1 = [[] for _ in range(n+1)]
    graph2 = [[] for _ in range(n+1)]
    for road in roads:
        s, e, c = road
        graph1[s].append((e, c))
        graph2[e].append((s, c))

    dfs(start, end, traps, graph1, visited, 0)

    return res
    

if __name__ == "__main__":
    print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
    print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))