import sys

sys.stdin = open('sample_input.txt')

def bt(n):
    global cnt, tree_info, node

    if n <= N: # n의 위치가 노드 개수보다는 적어야하니까
        bt(2*n) # 왼쪽으로 쭉 가다가 나오면
        tree_info[n] = node # 트리 인덱스에 노드 정보 넣어주고
        node += 1  # node 1 증가
        bt(2*n+1) #오른쪽으로 들어가기
    return


T = int(input())

for t in range(1, T+1):

    N = int(input())
    # 트리정보를 담은 리스트가 필요
    tree_info = [0 for _ in range(N+1)] # 노드 정보
    # 문제에서 tree의 구조를 살펴보면,
    # root는 항상 1이고
    # 왼쪽 노드의 위치는 부모노드의 2배이고
    # 오른쪽 노드의 위치는 부모노드의 2배+1임 이걸 이용해야함.

    # 어차피 무조건 1에 출발하고 계속 내려가는가 아닌가 이거니까.. 그 정지 규칙은
    # index가 노드의 갯수(N)보다 크다면 정지

    node = 1
    bt(1)
    print('#{} {} {}'.format(t, tree_info[1], tree_info[N//2]))


