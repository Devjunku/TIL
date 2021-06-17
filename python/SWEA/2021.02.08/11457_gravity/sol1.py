import sys

sys.stdin = open('input.txt')

def my_max(x):
    max_num = x[0]
    for i in range(1, len(x)):
        if max_num < x[i]:
            max_num = x[i]
    return max_num

T = int(input())
for t in range(1, T+1):
    N1 = int(input())
    numbers = list(map(int, input().split()))
    total = []
    for n in range(N1 - 2, -1, -1):
        cnt = 0
        for i in range(n + 1, N1):
            if numbers[n] > numbers[i]:
                cnt += 1
        total.append(cnt)
    print('#{0} {1}'.format(t, my_max(total)))





