import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))

    h_list = []

    for i in range(len(room)):
        h = 0
        for j in range(i+1, len(room)):
            k = 1
            while k < room[i][1] - room[i][0]:
                if room[j][0] <= room[i][0] + k <= room[j][1]:
                    h += 1
                    break
                k += 1
        h_list.append(h)
    print(h_list)

    h_list.sort()
    cnt = 0
    # for i in range(len(h_list)-1):
    #     if h_list[i] == h_list[i]:
    #         cnt += 1
    # print(max(h_list))



    print(max(h_list)+1)
    # print('#{} {}'.format(t, ))