ex = [-7, -3, -2, 5, 8]
N = len(ex)
for i in range(1<<N):
    ex_list = []
    for j in range(N):
        if i & (1<<j):
            ex_list.append(ex[j])
    if sum(ex_list) == 0:
        print(*ex_list)