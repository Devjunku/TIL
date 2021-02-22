import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    data = list(map(int,list(input())))
    # print(data)
    N = len(data)
    start = [0] * N
    cnt = 0
    i = 0
    while i < N:
        if data[i] == 1 and start[i] == 0:
            for j in range(i, N):
                start[j] = 1
            cnt += 1
        elif data[i] == 0 and start[i] == 1:
            for j in range(i, N):
                start[j] = 0
            cnt += 1
        i += 1
    print('#{} {}'.format(t, cnt))
    
    
            
    
    
    