# 입력값이 100,000으로 O(n**2)으로 했을 때 100,000,000이 넘어가므로
# 완전탐색으로 문제를 풀기보다 중복되는 부분을 제거해야한다.

import sys

# readline으로 읽는 경우 input처럼 한 줄 한 줄 입력값을 읽는 것이 아니 한번에 모두 읽어버리는 것이기 때문에
# 더 빠르게 시간을 단축시킬 수 있다.

n, m = map(int, sys.stdin.readline().split())
n_arr = [0]+list(map(int, sys.stdin.readline().split()))

# 1번째 원소부터 누적합 시킨다.
for k in range(1, len(n_arr)):
    n_arr[k] += n_arr[k-1]

# 이후 i와 j를 입력받으면서 각 구간을 합을 출력해준다.
# j번째까지 합 - i번째까지 합을 해주면 된다.
# 이때 누적합을 기록했기 때문에 n_arr를 index 슬라이싱 하므로
# O(1)로 접근이 가능하다.

for l in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(n_arr[j]-n_arr[i-1])