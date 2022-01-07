import sys

input = sys.stdin.readline

INF = int(1e9)

if __name__ == "__main__":
    n = int(input())
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i][i] = 0

    while True:
        s, e = map(int, input().split())

        if s == -1 and e == -1:
            break

        graph[s][e] = 1
        graph[e][s] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                print((i, j), (i, k), (k, j))
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    min_score = INF
    for i in range(1, n+1):
        min_score = min(min_score, max(graph[i][1:]))

    candidate = []
    for i in range(1, n+1):
        if min_score == max(graph[i][1:]):
            candidate.append(i)

    candidate.sort()

    print(min_score, len(candidate))
    print(" ".join(map(str, candidate)))




