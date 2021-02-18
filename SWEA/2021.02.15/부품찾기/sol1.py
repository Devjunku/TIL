def BS(arr, key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return False

N = 5
N_list = [8, 3, 7, 9, 2]
N_list.sort()

M = 3
M_list = [5, 7, 9]

for i in range(M):
    if BS(N_list, M_list[i]):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')