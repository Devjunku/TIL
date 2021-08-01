def solution(n, computers):

    def dfs(s):
        ch[s] = 1
        for e in a[s]:
            if ch[e] == 0:
                dfs(e)
    
    a = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if computers[i][j] == 1:
                a[i].append(j)
                a[j].append(i)

    ch = [0] * n
    c = 0

    for i in range(n):
        if ch[i] == 0:
            c += 1
            dfs(i)
    
    return c

if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    print(solution(5, [[1, 1, 0, 1, 0], [1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0]]))