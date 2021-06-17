import sys

sys.stdin = open('input.txt')

def MMVIndex(x):
    max_idx = 0
    min_idx = 0
    max_v = x[0]
    min_v = x[0]
    for i in range(1, len(x)):
        if x[i] > max_v:
            max_v = x[i]
            max_idx = i
        if x[i] < min_v:
            min_v = x[i]
            min_idx = i
    return [max_idx, max_v, min_idx, min_v]

for t in range(1, 11):
    N = int(input())
    box_list = list(map(int, input().split()))
    for n in range(N):
        MMVI = MMVIndex(box_list)
        box_list[MMVI[0]] -= 1
        box_list[MMVI[2]] += 1
    MMVI = MMVIndex(box_list)
    print('#{} {}'.format(t, MMVI[1]-MMVI[3]))

