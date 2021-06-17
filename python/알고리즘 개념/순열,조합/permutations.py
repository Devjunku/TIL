def permutations(arr, m):
    result = []

    if m == 0:
        return [[]]

    for idx, element in enumerate(arr):
        for j in permutations(arr[:idx] + arr[idx+1:], m-1):
            result += [[element]+j]

    return result