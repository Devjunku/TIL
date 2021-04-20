N = int(input())
K = int(input())

arr = [[] for i in range(N+1)]
for i in range(K):
   s, e = map(int, input().split())
   arr[s].append(e)
   arr[e].append(s)

def dfs(s, adj):
    stack = [s]
    visited = []
    while stack:
        w = stack.pop()
        visited.append(w)
        for u in adj[w]:
            if u not in visited + stack:
                stack.append(u)
    return visited

print(len(dfs(1, arr))-1)

