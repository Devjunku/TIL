import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A_List = list(map(int, input().split()))
    B_List = list(map(int, input().split()))

    toll = [0] * len(A_List)

    for i in range(len(B_List)):
        for j in range(len(A_List)):
            if B_List[i] >= A_List[j]:
                toll[j] += 1
                break
    
    idx = 0
    value = 0
    for i in range(len(toll)):
        if toll[i] > value:
            value = toll[i]
            idx = i
    print('#{} {}'.format(t, idx+1))

    