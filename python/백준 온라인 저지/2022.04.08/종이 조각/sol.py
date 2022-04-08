import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

answer = 0
for state in range(1 << n*m):
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    r = bin(state)[2:].zfill(n*m)
    print(r)
    for i in range(n):
        for j in range(m):
            visited[i][j] = r[i*m+j]

    score = 0
    for i in range(n):
        row = ""
        for j in range(m):
            if visited[i][j] == "1":
                row += str(arr[i][j])
            else:
                if row != "":
                    score += int(row)
                row = ""
        if row != "":
            score += int(row)
    
    for i in range(m):
        col = ""
        for j in range(n):
            if visited[j][i] == "0":
                col += str(arr[j][i])
            else:
                if col != "":
                    score += int(col)
                col = ""
        if col != "":
            score += int(col)
    
    answer = max(answer, score)

print(answer)