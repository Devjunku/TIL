import sys

sys.stdin = open('input.txt')

# T = int(input())
# buildings = list(map(int, input().split()))
# print(T)
# print(buildings)

def my_min(x):
    min_num = x[0]
    for i in range(1, len(x)):
        if min_num > x[i]:
            min_num = x[i]
    return min_num

for i in range(10):
    T = int(input())
    buildings = list(map(int, input().split()))
    total = 0
    for t in range(2,T - 2):
        scop = [buildings[t] - buildings[t-2],
                buildings[t] - buildings[t-1],
                buildings[t] - buildings[t+1],
                buildings[t] - buildings[t+2]]

        N = my_min(scop)
        if N > 0:
            total += N
    print('#{0} {1}'.format(i+1, total))
# idx = 0
# while idx < T-2:
#     if N > my_min(scop): 이렇게 바꿔도 됨.
#         total += N
#         idx += 3
#     else:
#         idx += 1
