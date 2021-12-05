from collections import deque

def solution(n, wires):
    answer = 100000
    graph = [[] for _ in range(n+1)]

    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    for node1, node2 in wires:
        visited = [False for _ in range(n + 1)]
        q = deque()
        q.append(node1)
        result = 1
        visited[node1] = True
        visited[node2] = True

        while q:
            node = q.popleft()
            for ele in graph[node]:
                if not visited[ele]:
                    result += 1
                    visited[ele] = True
                    q.append(ele)

        min_value = min(result, n-result)
        max_value = n - min_value
        if answer > max_value - min_value:
            answer = max_value - min_value

    return answer

if __name__ == "__main__":
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
    print(solution(4, [[1, 2], [2, 3], [3, 4]]))
    print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))


