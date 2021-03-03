import sys

sys.stdin = open('input.txt')


# def bfs(N_list):
#     queue = [N_list[0]]
#
#     while queue:
#         w = queue.pop(0)



for _ in range(1, 11):
    t = int(input())
    N_list = list(map(int, input().split()))
    # print(N_list)

    cnt = 1
    while True:
        w = N_list.pop(0)
        if w - cnt <= 0:
            N_list.append(0)
            break
        else:
            N_list.append(w - cnt)
            if cnt >= 5:
                cnt = 1
            else:
                cnt += 1
    print('#{} {}'.format(t, ' '.join(map(str, N_list))))