
# 나중에 풀자..

def solution(n, computers):
    adj = [[] for _ in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if j != i and computers[i][j] != 0:
                adj[i].append(j)

    stack = [0]
    stc = []
    visited = []
    while stack:
        u = stack.pop()
        visited.append(u)
        for w in adj[u]:
            if w not in visited + stack:
                visited.append(w)
                stack.append(w)
        if stack:
            stc.append([stack])
    print(visited)
    print(stc)

if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))