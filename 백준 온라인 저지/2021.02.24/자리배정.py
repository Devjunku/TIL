from sys import stdin

C, R = map(int, stdin.readline().rstrip().split())

K = int(stdin.readline().rstrip())

arr = [[0 for _ in range(C)] for _ in range(R)]

i = 1
r = 0
c = -1
direction = 1

while True:

    for _ in range(R):
        c += direction
        arr[c][r] = i
        if i == K:
            break
        i += 1

    if i == K:
        print(c+1,r+1)
        break 

    R -= 1
    C -= 1

    if R < 1 and C < 1:
        break

    for _ in range(C):
        r += direction
        arr[c][r] = i
        if i == K:
            break
        i += 1

    if i == K:
        print(c+1,r+1)
        break    
    direction = -direction