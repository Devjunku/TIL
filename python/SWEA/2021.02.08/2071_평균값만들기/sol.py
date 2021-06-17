import sys
sys.stdin = open('input.txt')

n = int(input())

for tc in range(1, n+1):
    m = list(map(int, input().split()))
    total = 0
    for j in range(len(m)):
        total += m[j]
    print('#{0} {1:.0f}'.format(tc, total/len(m)))