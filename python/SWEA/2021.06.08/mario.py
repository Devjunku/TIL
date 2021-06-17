n = int(input())
n_list = list(map(int, input().split()))
INF = int(1e9)
mapping = [INF] * n

d = [2, 7]


def dfs(m):
    global mapping

    if m == 0: return 0
    if m < 0: return int(-1e9)
    if mapping[m] != INF: return mapping[m]
    
    a = dfs(m-2)
    b = dfs(m-7)

    if a > b:
        mapping[m] = n_list[m] + n_list[m-2]
    else:
        mapping[m] = n_list[m] + n_list[m-7]
    
    return mapping[m]

dfs(n)
print(mapping)