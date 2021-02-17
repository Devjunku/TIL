N = int(input())

seq = list(map(int, input().split()))

for i in range(N):
    cnt = 0
    for j in range(len(seq)):
        if seq[i] <= seq[j]:
            cnt += 1
    print(len(seq)-cnt, end=' ')

