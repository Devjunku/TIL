import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # print(arr)
    
    # 90도 계산
    radi_90 = []
    for i in range(N):
        ex = []
        for j in range(len(arr)-1,-1,-1):
            ex.append(arr[j][i])
        radi_90.append(ex)
    
    # 180도 계산
    radi_180 = []
    for i in range(N-1, -1, -1):
        ex = []
        for j in range(N-1,-1,-1):
            ex.append(arr[i][j])
        radi_180.append(ex)

    # 270도 계산
    radi_270 = []
    for i in range(N):
        ex = []
        for j in range(len(arr)-1,-1,-1):
            ex.append(radi_180[j][i])
        radi_270.append(ex)

    print('#{}'.format(t))
    for k in range(N):
        res1 = ''.join(list(map(str, radi_90[k])))
        res2 = ''.join(list(map(str, radi_180[k])))
        res3 = ''.join(list(map(str, radi_270[k])))
        print('{} {} {}'.format(res1, res2, res3))