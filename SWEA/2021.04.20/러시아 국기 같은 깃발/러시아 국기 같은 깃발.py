import sys

sys.stdin = open('sample_input.txt')

color_list = ['W', 'B', 'R']

def dfs(idx, color_idx, total):
    global change, arr

    if change <= total:
        return

    if idx >= N-1:
        if change >= total:
            change = total
            return
    
    for i in range(color_idx, min(3, color_idx+2)):
        cnt = 0

        if idx >= N-2 and i == 0:
            continue

        for color in arr[idx]:
            if color != color_list[i]:
                cnt += 1

        dfs(idx+1, i, total+cnt)


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]
    change = 99999
    dfs(1, 0, 0)

    for w in arr[0]:
        if w != 'W':
            change += 1
    for r in arr[N-1]:
        if r != 'R':
            change += 1

    print(f'#{t} {change}')