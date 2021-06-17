import sys

sys.stdin = open('sample_input.txt')

def tree_sort(n):
    global tree
    if n >= 2:
        if tree[n] < tree[n // 2]:
            tree[n], tree[n // 2] = tree[n//2], tree[n]
            tree_sort(n//2)


# 이문제도 역시 root의 index는 1임
T = int(input())

for t in range(1, T+1):
    N = int(input())
    tree = [0]
    node_info = list(map(int, input().split()))
    for i in node_info:
        tree.append(i)
        tree_sort(len(tree)-1)
    print(tree)

    res = 0
    i = len(tree)-1
    if i < 2:
        continue
    else:
        i //= 2
        while i > 0:
            res += tree[i]
            i //= 2

    print('#{} {}'.format(t, res))