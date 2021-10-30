import sys
input = sys.stdin.readline
# from itertools import combinations

N, S = map(int, input().split())
seq = list(map(int, input().split()))

# def combinations(arr, m):

#     result = []
#     if m == 0:
#         return [[]]
    
#     for idx in range(len(arr)):
#         element = arr[idx]
#         arr_ele = arr[idx+1:]
#         for j in combinations(arr_ele, m-1):
#             result.append([element] + j)

#     return result

# cnt = 0
# for i in range(1, N+1):
#     comb = combinations(seq, i)
#     for com in list(comb):
#         if sum(com) == S:
#             cnt += 1

# print(cnt)
cnt = 0
def dfs(idx, Sig):
    global cnt

    if idx >= N:
        return
    
    Sig += seq[idx]

    if Sig == S:
        cnt += 1
    dfs(idx + 1, Sig - seq[idx])
    dfs(idx + 1, Sig)

dfs(0, 0)
print(cnt)