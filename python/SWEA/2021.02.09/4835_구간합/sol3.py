T = int(input())

for tc in range(1, T+1):
    # N : 원소의 개수
    # M : 구간의 길이
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    tmp = 0
    for i in range(M):
        tmp += nums[i]

    max_value = tmp
    min_value = tmp
    for i in range(M, N):
        tmp = tmp + nums[i] - nums[i-M]
        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

