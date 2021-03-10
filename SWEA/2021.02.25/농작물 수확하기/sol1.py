import sys

sys.stdin = open('input.txt')



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, list(input()))))


    half = len(arr) // 2

    idx_list_col = list(range(0, half+1)) + list(range(half-1, -1,-1))
    idx_list_row = list(range(len(arr)))
    print(idx_list_col)
    print(idx_list_row)
    res_list = 0
    for c, r in zip(idx_list_col, idx_list_row):
        if c == 0:
            res_list += arr[half][r]
        else:
            res_list += arr[half][r]
            j = 1
            while j <= c:
                res_list += arr[half-j][r]
                res_list += arr[half+j][r]
                j += 1
    print('#{} {}'.format(t, res_list))

















