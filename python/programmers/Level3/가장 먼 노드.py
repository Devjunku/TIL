from collections import deque


def solution(n, edge):
    
    adj = [[] for _ in range(n+1)]
    visited = [ 0 for _ in range(n+1)]

    for i in range(len(edge)):
        adj[edge[i][0]].append(edge[i][1])
        adj[edge[i][1]].append(edge[i][0])

    queue = deque()
    queue.append(1)
    stack = []
    while queue:
        stack_1 = []
        while queue:
            u = queue.popleft()
            visited[u] = 1
            for v in adj[u]:
                if visited[v]:
                    continue
                stack_1.append(v)
                visited[v] = 1
        queue.extend(stack_1)
        if queue:
            pass
        else:
            break
        stack = stack_1
    return len(stack)



if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))