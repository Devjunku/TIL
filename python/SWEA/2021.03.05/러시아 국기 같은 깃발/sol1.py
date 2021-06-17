def color(i, c):
    result = 0

    for j in range(M):
        if flags[i][j] != c:
            result += 1

    return result


def count(a, b):
    result = 0

    for i in range(0, N):
        if i < a:
            result += color(i, 'W')
        elif a <= i < b:
            result += color(i, 'B')
        else:
            result += color(i, 'R')

    return result


def dfs(L, s):
    global answer
    if L == 2:
        result = count(res[0], res[1])
        if answer > result:
            answer = result
        return
    else:
        for i in range(s, len(nums)):
            res[L] = nums[i]
            dfs(L + 1, i + 1)


T = int(input())
for t in range(1, 1 + T):
    N, M = map(int, input().split())
    flags = [list(input()) for _ in range(N)]
    nums = [i for i in range(N) if i]

    res = [None, None]
    answer = 999999999999

    dfs(0, 0)

    print(f'#{t} {answer}')