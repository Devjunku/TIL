# 합병정렬릉 그냥 두 부분으로 나누는 반면에, 퀵정렬은 분할할 때,
# 기준 아이템(pivot item) 중심으로, 이 보다 작은 것은 왼편,
# 큰 것은 오른편에 위치시킨다.

# 각 부분 정렬이 끝난 후, 합병정렬은 '합병'이란 후처리
# 작업이 필요한, 퀵정렬은 필요로 하지 않는다.

# ex

def quickSort(a, begin, end):
    if begin < end:
        p = partition = (a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)

# 호어 파티션
def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    
    while L < R:
        while (a[L] < a[pivot] and L < R):
            L += 1

        while (a[L] >= a[pivot] and L < R):
            R -= 1

        if L < R:
            if L == pivot: pivot = R
            a[L], a[R] = a[R], a[L]

    a[pivot], a[R] = a[R], a[pivot]

    return R