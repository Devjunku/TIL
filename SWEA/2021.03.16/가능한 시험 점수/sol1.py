import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    res = []
    for i in range(1<<N):
        ex_list = []
        for j in range(N):
            if i & (1<<j) and score[j]:
                ex_list.append(score[j])
                if not ex_list:
                    continue
                else:
                    a = sum(ex_list)
                    if sum(ex_list) not in res:
                        res.append(a)
    print('#{} {}'.format(t, len(res)+1))



