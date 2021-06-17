ex_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1<<len(ex_set)):
    total = []
    for j in range(len(ex_set)):
        if i & (1<<j):
            total.append(ex_set[j])

    if sum(total) == 10:
        print(*total)
        break

##############################################

data = list(range(1, 11))

is_selected = [None] * len(data)
results = []

def power_set(idx): # 이렇게 짠 함수는 잘 짠 함수는 아님
    # is_selected를 다 채우지 못했다면
    if idx < len(data):
        is_selected[idx] = True
        power_set(idx + 1)
        is_selected[idx] = False
        power_set(idx + 1)
    # 다 채웠다면
    else: #idx < len(data)
        total = 0
        for i in range(len(data)):
            if is_selected[i]:
                total += data[i]
        if total == 10:
            results.append(is_selected[:])
        return None

power_set(0)

for result in results:
    print(result)