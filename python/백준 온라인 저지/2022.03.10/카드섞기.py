import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
p_seq = list(map(int, input().split()))
s_seq = list(map(int, input().split()))

origin = deepcopy(p_seq)
g_seq = [0, 1, 2] * (n // 3)

new = [0] * n
cnt = 0

while p_seq != g_seq:
    for i in range(n):
        new[s_seq[i]] = p_seq[i]
    
    p_seq = deepcopy(new)
    new = [0] * n
    cnt += 1

    if origin == p_seq:
        cnt = -1
        break

print(cnt)