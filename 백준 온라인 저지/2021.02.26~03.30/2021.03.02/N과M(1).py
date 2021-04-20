N, M = map(int, input().split())

N_list = list(range(1, N+1))

from itertools import permutations

for ans in permutations(N_list, M):
    print(*ans)