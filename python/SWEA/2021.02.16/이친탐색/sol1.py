import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def BS(P, key):
    start = 1
    cnt = 0
    end = P
    while start <= end:
        mid = (start + end) // 2
        cnt += 1
        if mid == key:
            break
        elif mid < key:
            start = mid
        else:
            end = mid
    return cnt

for t in range(1, T+1):
    P, A, B = map(int, input().split())
    A_cnt = BS(P, A)
    B_cnt = BS(P, B)
    if A_cnt > B_cnt:
        print('#{} B'.format(t))
    elif A_cnt < B_cnt:
        print('#{} A'.format(t))
    else:
        print('#{} 0'.format(t))





