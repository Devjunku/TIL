# from sys import stdin

# N, K = map(int, stdin.readline().rstrip().split())
# temp_list = list(map(int, stdin.readline().rstrip().split()))

# sum_temp = sum(temp_list[0:K])
# res = sum_temp

# if K == 1:
#     print(max(temp_list))
# else:
#     i = 0
#     while i < N-K+1:
#         sum_temp -= temp_list[i]
#         sum_temp += temp_list[i+K]
#         if res < sum_temp:
#             res = sum_temp
#         i+=1
#     print(res)


from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())
temp_list = list(map(int, stdin.readline().rstrip().split()))

sum_temp = sum(temp_list[0:K])
res = sum_temp

for i in range(N-K):
    sum_temp -= temp_list[i]
    sum_temp += temp_list[i+K]
    if res < sum_temp:
        res =  sum_temp
print(res)
