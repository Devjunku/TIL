import sys
sys.stdin = open("input.txt")

T = int(input())


dx = [-1, 1]
dy = [-1, 1]

def abbs(x, y):
    if x >= y:
        return x - y
    else:
        return y - x

for tc in range(1, T+1):
    arr = []
    N = int(input())
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(dx)):
                if -1 < j + dx[k] < len(arr):
                    cnt += abbs(arr[i][j], arr[i][j + dx[k]])
                if -1 < i + dy[k] < len(arr):
                    cnt += abbs(arr[i][j], arr[i+dy[k]][j])
    print('#{} {}'.format(tc, cnt))


    # print("#{} {}".format(tc, ))







