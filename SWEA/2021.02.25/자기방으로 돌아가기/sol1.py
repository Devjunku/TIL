import sys

sys.stdin = open('sample_input.txt')
# 2021.03.10 복습할 때의 풀이 
T = int(input())

for t in range(1, T+1):
    room = [0] * 201
    N = int(input())

    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        for i in range((s//2+s%2), (e//2+e%2)+1):
            room[i] += 1
        
    print('#{} {}'.format(t, max(room)))
        

# 원래 풀이
# T = int(input())

# aisle = [0] * 201

# for t in range(1, T+1):
#     aisle = [0 for _ in range(201)]
#     N = int(input())
#     S = []
#     E = []
#     for _ in range(N):
#         s, e = map(int, input().split())
#         if s > e:
#             s, e = e, s
#         S.append((s+1)//2)
#         E.append((e+1)//2)
    
#     for start, end in zip(S, E):
#         for i in range(start, end+1):
#             aisle[i] += 1

#     print('#{} {}'.format(t, max(aisle)))