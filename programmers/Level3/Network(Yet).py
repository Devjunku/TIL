def DFS(adj, v, hist):
    hist.append(v)
    for i in range(len(adj)):
        if adj[v][i] and i not in hist:
            hist = DFS(adj, i, hist)
    return hist


def solution(n, computers):
    for i in range(n):
        computers[i][i] = 0
    
    ans = 1
    for k in range(n-1):
        if DFS(computers, k, []).sort() != DFS(computers, k+1, []).sort():
           ans += 1 

    return ans



if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    