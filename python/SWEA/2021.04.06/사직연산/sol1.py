import sys

sys.stdin = open('input.txt')


def bt_bfs(n):

    if n >= N: # 정지 규칙
        return

    if tree[n][2] != 0:
        bt_bfs(tree[n][2]) # 왼쪽으로!
    if tree[n][3] != 0:
        bt_bfs(tree[n][3]) # 오른쪽으로!

    # 다 빠져나왔으면, 해당 연산자를 추출(문제 조건상 없을 수 없음)
    oper = tree[n][1]

    # 연산자 검사한후 업데이트
    if oper == '/':
        tree[n][1] = tree[tree[n][2]][1] / tree[tree[n][3]][1]

    elif oper == '*':
        tree[n][1] = tree[tree[n][2]][1] * tree[tree[n][3]][1]

    elif oper == '+':
        tree[n][1] = tree[tree[n][2]][1] + tree[tree[n][3]][1]

    elif oper == '-':
        tree[n][1] = tree[tree[n][2]][1] - tree[tree[n][3]][1]


for t in range(1, 11):
    N = int(input())

    # 교수님 풀이처럼 4개로 해서 정보를 받고
    tree = [[0] * 4 for _ in range(N+1)]

    for _ in range(N):
        info = list(input().split())
        if info[1].isdigit():
            tree[int(info[0])][1] = int(info[1]) # 연산자는 따로 추가, 없으면, 0임
        else:
            tree[int(info[0])][1] = info[1]
            tree[int(info[0])][2] = int(info[2])
            tree[int(info[0])][3] = int(info[3])

    bt_bfs(1)
    print('#{} {}'.format(t, int(tree[1][1])))







