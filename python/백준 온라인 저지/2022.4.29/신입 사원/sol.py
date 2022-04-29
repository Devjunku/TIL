import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[0])

    mv = arr[0][1]
    cnt = 1

    for i in range(1, n):
        if mv > arr[i][1]:
            mv = arr[i][1]
            cnt += 1
    
    print(cnt)
        