import sys

sys.stdin = open('input.txt')


def dfs(n):
    global res, char, edge_list

    if not edge_list[n]:
        res += char[n - 1]
        return

    if len(edge_list[n]) == 2:
        dfs(edge_list[n][0])
        res += char[n - 1]
        dfs(edge_list[n][1])

    if len(edge_list[n]) == 1:
        dfs(edge_list[n][0])
        res += char[n - 1]


for t in range(1, 10+1):

    V = int(input())
    edge_list = [[] for _ in range(V+1)]
    char = []

    for _ in range(V):
        edge = list(map(str, input().split()))
        char.append(edge[1])

        i = 2
        while len(edge) - 2:
            edge_list[int(edge[0])].append(int(edge[i]))
            i += 1
            if i >= len(edge):
                break

    res = ''
    dfs(1)
    print('#{} {}'.format(t, res))



