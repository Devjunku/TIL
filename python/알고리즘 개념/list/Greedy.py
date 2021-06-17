# 탐욕 알고리즘은 최적해를 구하는 데 사용되느느 근시안적인 방법
# 여러 경우 중 하나를 결정해야 할 때마다 그 순간, 최적이라고 생각되는 것을 선택해 나가는 방식
# 각 선택의 시점에서 이루어지는 결정은 지역적으로 최적
# 하지만, 전역해는 아닐 수 있음
# 즉 최적이라는 보장은 없음

# 일반적으로 머릿속에 떠오르는 생각을 검즈 없이 바로 구현하면
# GREEDY 접근이 됨.

# 예를 들어서 거스름돈 줄이기 같은 경우임

# SWEA의 View 문제도 Greedy의 일종
# 풀이
def my_min(x): # 최소값 함수 작성
    min_num = x[0]
    for i in range(1, len(x)):
        if min_num > x[i]:
            min_num = x[i]
    return min_num

for i in range(10):
    T = int(input())
    buildings = list(map(int, input().split()))
    total = 0
    for t in range(2,T - 2):
        scop = [buildings[t] - buildings[t-2],
                buildings[t] - buildings[t-1],
                buildings[t] - buildings[t+1],
                buildings[t] - buildings[t+2]]
            # SCOP 중에서 
        N = my_min(scop) # 가장 작은 것을 선택하면 View 층 갯수가 나타남.
        if N > 0:
            total += N # 전체 total에 더하기
    print('#{0} {1}'.format(i+1, total))