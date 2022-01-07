n = int(input())
m = int(input())

# 분기 처리는 하는 이유는 n = 1이면 그냥 1이기 때문입니다.
# 하지만 n = 2 이 경우는 달라요. 그러면 방법의 수가 1일수도 있고 2일수도 있습니다. 그래서 분리하는 겁니다.
if n >= 2:
    # 미리 연속된 좌석에 의한 방법의 수를 기록해 놓습니다.
    # 이건 아무도 vip가 없다는 가정하에 n이 최대입니다.

    dp = [1 for _ in range(n + 1)]
    #  2번째는 무조건 2입니다.
    dp[2] = 2

    # dp 계산해줍시다.
    # 계차수열의 점화식입니다.
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # 밑의 데이터는 vip에요. vip 데이터를 받고 아래와 같은 코드를 통해 구간을 구해줍니다.
    i = 1
    answer = []
    for _ in range(m):
        idx = int(input())
        answer.append(idx - i)
        i = idx + 1
    answer.append(n - i + 1)

    # 미리 만든 dp를 통해 계산해줍시다.
    res = 1
    for a in answer:
        res *= dp[a]
    print(res)
else:
    for _ in range(m):
        v = int(input())
    print(1)