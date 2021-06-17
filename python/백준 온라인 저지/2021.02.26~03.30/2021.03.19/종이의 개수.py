N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

minus = 0
zero = 0
one = 0
def div(start_x, end_x, start_y, end_y):
    global arr, minus, zero, one
    n = (start_x - end_x)**2

    minus_cnt = 0
    zero_cnt = 0
    one_cnt = 0

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if arr[i][j] == -1:
                minus_cnt += 1
            elif arr[i][j] == 0:
                zero_cnt += 1
            else:
                one_cnt += 1
    
    if minus_cnt == n:
        minus += 1
        return 
    elif zero_cnt == n:
        zero += 1
        return
    elif one_cnt == n:
        one += 1
        return

    div(start_x, end_x//3, start_y, end_y//3)
    div(start_x, end_x//3, end_y//3, 2*(end_y//3))
    div(start_x, end_x//3, 2*(end_y//3), end_y)
    div(end_x//3, 2*(end_x//3), start_y, end_y//3)
    div(end_x//3, 2*(end_x//3), end_y//3, 2*(end_y//3))
    div(end_x//3, 2*(end_x//3), 2*(end_y//3), end_y)
    # div(2*(end_x//3), end_x, start_y, end_y//3)
    # div(2*(end_x//3), end_x, end_y//3, 2*(end_y//3))
    # div(2*(end_x//3), end_x, 2*(end_y//3), end_y)

div(0, N, 0, N)

print(minus)
print(zero)
print(one)