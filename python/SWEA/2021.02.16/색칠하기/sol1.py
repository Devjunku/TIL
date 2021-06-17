import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = [[0 for _ in range(10)] for _ in range(10)]

    color_arr = []
    color = []
    for _ in range(N):
        area = list(map(int, input().split()))
        color_arr.append(area[:-1])
        color.append(area[-1])
    # print(color_arr)
    for i in range(len(color_arr)):
        for j in range(color_arr[i][0], color_arr[i][2]+1):
            for k in range(color_arr[i][1], color_arr[i][3]+1):
                arr[j][k] += color[i]
    cnt = 0

    # for i in range(len(arr)):
    #     print(arr[i])


    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(t, cnt))


