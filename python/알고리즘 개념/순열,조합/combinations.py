def combinations(arr, m):
    result = []

    if m == 0:
        return [[]]
    
    for idx in range(len(arr)):
        element = arr[idx]
        arr_ele = arr[idx+1:]
        for j in combinations(arr_ele, m-1):
            result.append([element]+j)
            
    return result