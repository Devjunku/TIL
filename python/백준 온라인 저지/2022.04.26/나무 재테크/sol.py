import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
S2D2 = [list(map(int, input().split())) for _ in range(n)]
nutri = [[5 for _ in range(n)] for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)


dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

for _ in range(k):


    # TODO 봄 + 여름
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                alive_tree, dead_tree = [], 0
                for age in tree[i][j]:
                    if age <= nutri[i][j]:
                        nutri[i][j] -= age
                        age += 1
                        alive_tree.append(age)
                    else:
                        dead_tree += age//2
                nutri[i][j] += dead_tree
                tree[i][j].clear()
                tree[i][j].extend(alive_tree)
    
    if not tree:
        print(0)
        exit()
    
    # TODO 가을
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for d in range(8):
                            nx, ny = i + dx[d], j + dy[d]
                            if not (0 <= nx < n and 0 <= ny < n): continue
                            tree[nx][ny].append(1)
    
    # TODO 겨울
    for i in range(n):
        for j in range(n):
            nutri[i][j] += S2D2[i][j]
    
    
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])

print(answer)