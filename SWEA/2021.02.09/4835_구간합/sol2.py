T = int(input())

for tc in range(1, T+1):
    # N : 원소의 개수
    # M : 구간의 길이
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    max_value = 0
    min_value = 987654321

    for i in range(N-N+1):
        tmp = 0
        for j in range(M):
            tmp += nums[i+j]

        # for j in nums[i:i+M]:
        #     tmp += j

        if max_value < tmp:
            max_value = tmp

        if min_value > tmp:
            min_value tmp

    print('#{} {}'.format(tc, max_value-min_value))
