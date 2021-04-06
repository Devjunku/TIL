import sys

sys.stdin = open('sample_input.txt')


def preorder(n):
    global cnt
    if n > 0:
        preorder(left[n])
        preorder(right[n])
        cnt += 1

T = int(input())

for t in range(1, T+1):

    E, N = map(int, input().split())
    node_info = list(map(int, input().split()))

    max_e = max(node_info)
    left = [0]*(max_e+1)
    right = [0]*(max_e+1)

    for i in range(len(node_info)//2):
        n1, n2 = node_info[2*i], node_info[2*i+1]
        if left[n1] == 0:
            left[n1] = n2
        else:
            right[n1] = n2

    # print(left)
    # print(right)


    cnt = 0

    # N을 루트로 한다고 문제에서 그랬으니 parent를 안해도 괜찮음
    preorder(N)
    print('#{} {}'.format(t, cnt))
