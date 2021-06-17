import sys

sys.stdin = open('sample_input.txt')


color_list = ['W', 'B', 'R']

# 백트래킹? 문제,'최소 배열 합' 과 비슷..?
# 우선 문제의 조건에 따라 처음 행과 마지막 행은 무조건 'W', 'R'로 가야함
# 이를 이용해 그 밖의 행만 조절하는 것으로 진행
# 따라서 시작 행은 1이 됨
def dfs(idx, color_idx, total):
    # 시작할 인데스(idx) # 1로 시작
    # color_list를 통제하기 위한 변수(color_idx) # 0 시작
    # 카운트를 반영할 (total) # 0 시작
    global change, arr # 관여할 global 변수들

    if change <= total: # total이 change보다 크면 볼 필요가 없음
        return # (의미없는 연산을 피하기 위해 return)

    if idx >= n-1: # 인덱스가 넘어가면 역시나 볼 필요 없음
        if total <= change: # change가 total보다 크면
            change = total # change를 total로 바꿔야함 안그러면 초기값 설정으로 인해 change값이 너무 큼
            return # 역시나 재귀를 멈추기 위해 return

    for i in range(color_idx, min(3, color_idx+2)): # 이 for 구문에서 color_list를 하나씩 증가하면서 idx에 적용해야함.
        cnt = 0 # color_idx의 인덱스는 0~2까지니까 min()을 활용해서 3까지 볼 수 있도록 해야함.
                # color_idx+2를 하는 이유는 1행부터 n-2행까지 'R'가 들어가지 않은 경우를 보기 위함
        if idx >= n-2 and i == 0: # idx가 n-2보다 크거나 같으면 무조건 'B'가 들어가야 하고
            continue # i = 0 이면 'W'임. 즉 'R'전에 무조건 'B'가 들어가야 하는데
                     # 저 조건을 주지 않으면 'W'와 'R' 사이에 'B'를 넣을 수 없음
                     # 그래서 conintue, 볼 필요 없는 것임
        for color in arr[idx]: # 이제 해당 행을 읽으면서
            if color_list[i] != color: # color 색이랑 같지 않으면
                cnt += 1 # 카운트
        dfs(idx+1, i, total + cnt) # 행 인덱스만 증가시킨채로 재귀로 들어감
                                   # 여기서 나오면 i만 증가한 채로 다시 재귀가 들어감
                                   # 즉 얘의 역할은 중복 조합의 역할을 함
                                   # 앞의 if >= n-2 and i == 0 에서
                                   # 조합하면 안될 것을 걸러주기 때문에 문제의 조건을
                                   # 만족시킬 수 있음.

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    change = 99999
    dfs(1, 0, 0)
    for w in arr[0]: # 0행과 n-1행은 안봤으니까. 적용해주기
        if w != 'W':
            change += 1 # 무조건 'W'
    for r in arr[n - 1]:
        if r != 'R':
            change += 1 # 무조건 'R'
    print('#{} {}'.format(t, change))
