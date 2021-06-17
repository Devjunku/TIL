import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def selectSorting(x):
    for i in range(0, len(x)-1):
        min_idx = i
        for j in range(1+i, len(x)):
            if x[min_idx] > x[j]:
                min_idx = j
        x[min_idx], x[i] = x[i], x[min_idx]
    return x

for t in range(1, T+1):

    N = int(input())

    test_list = list(map(int, input().split()))

    res = selectSorting(test_list)
    ans = ''
    for i in range(5):
        ans += str(res[-i -1]) + ' '
        ans += str(res[i]) + ' '

    print('#{} {}'.format(t, ans[0:len(ans)-1]))


