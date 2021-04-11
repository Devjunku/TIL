import sys

sys.stdin = open('sample_input.txt')


def tree_sorting(n):
    global tree
    if n >= 2:
        if tree[n] < tree[n // 2]:
            tree[n], tree[n // 2] = tree[n//2], tree[n]
            tree_sorting(n//2)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    node = list(map(int, input().split()))

    tree = [0]
    for i in node:
        tree.append(i)
        tree_sorting(len(tree)-1)

    res = 0
    n = len(tree)-1
    if n <= 2:
        continue
    else:
        while n > 0:
            n //= 2
            res += tree[n]
            
    print(f'#{t} {res}')