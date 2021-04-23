import sys

sys.stdin = open('sample_input.txt')

'''
사실 상 서로소 문제인데, 라이브 강의에서 처음 들었을 때
이해가 바로가지 않아서 개인적으로 갖고 있는 책을 보았던게 도움이 됐다.

사실 prim과 크루스칼 알고리즘의 가장 기초적인 형태로 머릿속에 정리가 되어 있는데
아직 모든걸 이해하고 있지는 않다.

그렇다보니, 부모 루트를 찾고 합치기 이러한 과정을 거쳐서 결국 하나의 통합된
형태로 진행하는 것이구나라고 정리를 마친 상태이지만 아직 감이 잘 잡힌 형태는 아니기 때문에
지속적인 복습이 필요하다.

어려운 문제는 아니지만, 개념 정리가 필수인 그런 문제였다.
'''

# 부모 합치기
def union(idx1, idx2):
    n1, n2 = find_parent(idx1), find_parent(idx2)

    if level[n1] >= level[n2]:
        pa[n2] = n1
    else:
        pa[n1] = n2
    
    # 이 부분은 '번호를 적지도 않고
    # 다른 사람에게 지목되지도 않은 사람은
    # 단독으로 조를 구성하게 된다.'
    # 를 반영하기 위해서 
    if level[n1] == level[n2]:
        level[n1] += 1

# 부모 찾기
def find_parent(idx):
    if pa[idx] != idx:
        return find_parent(pa[idx])
    else:
        return idx

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))
    level = [0] * (N+1)
    pa = [n for n in range(N+1)]

    # 계속 부모 합치기 (그러면 수렴되는 부모들이 있음)
    for i in range(M):
        union(info[2*i], info[2*i+1])

    # 이를 set으로 중복 없애기
    groups = set()
    for i in range(1, 1+N):
        groups.add(find_parent(i))
    
    print(f'#{t} {len(groups)}')