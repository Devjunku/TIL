import sys

sys.stdin = open('input.txt')

T = int(input())

dic = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}




for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(str, list(input()))) for _ in range(N)]

    for n in range(N):
        for m in range(M):
            if arr[n][m] == '1':
                ex, ey = n, m

    # print(n, m)

    password = ''.join(arr[ex][(ey-55):ey+1])
    # print(password)

    k = 1
    f = 0
    s = 0
    for i in range(0, 56, 7):
        num = dic[password[i:i+7]]
        if k:
            f += num 
            k = 0
        else:
            s += num
            k = 1
    
    if not (3*f + s) % 10:
        print(f'#{t} {f+s}')
    else:
        print(f'#{t} {0}')