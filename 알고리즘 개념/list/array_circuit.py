# row (Square Two-Dimension)

for i in range(len(Array)):
    for j in range(len(Array)):
        print(Array[i][j])

# col (Square Two-Dimension)

for i in range(len(Array)):
    for j in range(len(Array)):
        print(Array[j][i])

# diagonal (Square Two-Dimension)

for i in range(len(Array)):
    print(Array[i][i]) # 정방향
    print(Array[i][len(Array)-1-i]) # 역방향

# zigzag (Two-Dimension)

for i in range(len(Array)):
    for j in range(len(Array[0])):
        print(Array[i][j + (m-1-2*j) * (i % 2)])

# Searching Two Dimension Array using delta

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(len(Array)):
    for u in range(len(Array[x])):
        for i in range(4):
            testX = x + dx[mode]
            testY = y + dy[mode]
            test(Array[testX][testY])

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

r = 0
c = 1
N = 3

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

drc = zip(dr, dc)

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    
    # if nr < 0 or nr >= N or nc < 0 or nc >= N:
        # continue
    # print(arr[nr][nc])

    if 0 <= nr < N  and 0 <= nc < N:
        print(arr[nr][nc])

# 전치행렬

# i 행의 좌표 len(arr)
# j 열의 좌표 len(arr[0])
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i > j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


# 비트 연산자를 이용한 부분집합

arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end = ', ')
        print()
    print()

