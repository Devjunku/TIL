N = int(input())
N_list = sorted(list(map(int, input().split())))
div, mod = divmod(N, 2)
print(N_list[div-1])