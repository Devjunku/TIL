import sys

sys.stdin = open('input.txt')

'''
최소 거리를 구하는 문제이기 때문에 다익스트라 알고리즘 문제이다.

이 문제 2021 카카오 블라인드 채용 문제인
'합승 택시 요금'(프로그래머스에 있음)와 아주 유사하다

물론 혼자서 못 풀었다.

아직 다익스트라를 구현할수가 없어서..

하지만 어느 정도 감을 잡기 시작했다.

예를 들어 대표적인 트리문제들은 간선정보를 주었을 때
주어진 정보를 이용하여 graph를 만들어야한다.
이를 이용해서 문제를 풀이하는 방식이 많은거 같다.(느낌상..)

받은 정보를 토대로 info_edge()에 넣어줘서 graph를 만든다.
물론 다익스트라의 경우 우선순위 큐로 진행하기 때문에
이를 활용한다. 따라서 python 모듈 중에 heapq를 활용
또한 priorityQueue라는 모듈도 있다고 들었는데,

heapq와 priorityQueue 중 heapq가 더 빠르게 작동한다고 한다.
따라서 이를 이용하자.

그리고 아직 heapq의 구동 방식을 완전히 이해하진 못했지만,
조금씩 감을 잡고 있는 중이다. 알고리즘 수업 끝났다고 멈추지 말고
하루에 2개씩 풀어보자.. 꾸준히.. ㅜ
'''



import heapq

# 노드 정보 만들기
def info_edge():
    for i in range(N):
        for j in range(i+1, N):
            distance = ((y_location[i] - y_location[j])**2 + (x_location[i] - x_location[j])**2)*tax_rate
            heapq.heappush(dist, (distance, i, j))

# 부모 찾기
def who_parent(x):
    if parent[x] != x:
        parent[x] = who_parent(parent[x])
    
    return parent[x]

# 부모 합치기
def union_parent(x, y):
    p1, p2  = who_parent(x), who_parent(y)
    
    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1

# 사이클인가?
def is_equal(x, y):
    return who_parent(x) == who_parent(y)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    x_location = list(map(int, input().split()))
    y_location = list(map(int, input().split()))
    tax_rate = float(input())
    
    dist = []
    parent = [i for i in range(N)]

    info_edge()
    res = 0 # 여기에 답을 낼거임
    cnt = 0 

    # dist에 원소가 없거나 최대 간선 개수를 넘어서면 루핑을 멈출 것임
    while dist and cnt != N-1:
        d, i, j = heapq.heappop(dist)

        # 사이클이 형성되지 않으면
        if not is_equal(i, j):
            # 거리는 res에 cnt는 1을 더하기!
            res += d
            cnt += 1
            # 부모 합쳐주고
            union_parent(i, j)

    # 문제에서 반 올림이라고 했으므로 0.5 더하고 int 씌우자
    # 개 꿀팁!
    res = int(res+0.5)

    print(f'#{t} {res}')