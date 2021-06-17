'''
5 6
1 2 1 3 3 2 3 4 2 5 5 4
'''

V, E = map(int, input().split())
edge = list(map(int, input().split()))

adj = [[0]*(V+1) for _ in range(V+1)]
adjlist = [[]for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

    adjlist[n1].append(n2)
    adjlist[n2].append(n1) # 무향인 경우에만

print()