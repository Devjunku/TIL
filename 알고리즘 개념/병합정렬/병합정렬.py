def merge_sort(arr):

    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])

    merge_list = []
    l = r = 0

    while l < len(left_list) and r < len(right_list):
        if left_list[l] <= right_list[r]:
            merge_list.append(left_list[l])
            l += 1
        else:
            merge_list.append(right_list[r])
            r += 1
        
    merge_list += right_list[r:]
    merge_list += left_list[l:]

    return merge_list

arr = [5, 7, 9, 1, 4, 3, 9, 2]
print(merge_sort(arr))
print(sorted(arr))