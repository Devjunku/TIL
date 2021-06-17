# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# 크게 3가지?
# 2차원 배열 입력 받는 법
# N, M = map(int, input().split())

# arr = [0] * N

# for i in range(N):
#     arr[i] = list(map(int, input().split()))

# arr = [list(map(int, input().split())) for _ in range(N)]

# for i in arr:
#     print(i)

# 배열 순회
# 1. 행 우선 순회
# 2. 열 우선 순회
# 3. 역 방향 행 순회
# 4. 역 방향 열 순회
# 5. 지그재그
# 6. 달팽이 순회

# 1. 행 우선 순회

# for i in range(len(Array)):
#     for j in range(len(Array[i])):
#         Array[i][j]


# 행 우선 순위
# arr = [[1,2,3,4],
#        [5,6,7,8],
#        [10,11,12,13]]

# N = 3
# M = 4
# len(arr)
# len(arr[0])
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j])

# 열 우선 순위

# for j in range(len(Array[0])):
#     for j in range(len(Array)):
#         Array[i][j]

# 행 역순으로 순회
# for i in range(N):
#     for j in range(M-1, -1, -1):
#         print(arr[i][j])

# 지그재그 순회

# for i in range(len(Array)):
#     for j in range(len(Array[0])):
#         Array[i][j + (m-i-2*j)*(i % 2)]

# 델타를 이용한 2차 배열 탐색

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for x in range(len(arr)):
#     for y in range(len(arr[x])):
#         for i in range(4):
#             textX = x + dx[mode]
#             textY = y + dy[mode]
#             test(arr[textX][textY]) # text라는 함수를 실행시켰다.

# arr = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]

# r = 1
# c = 1
# N = 3

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# for i in range(4):
#     nr = r+dr[i]
#     nc = c+dc[i]

# if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
# print(arr[nr][nc])

#     if 0 <= nr < N and 0 <= nc < N:
#         print(arr[nr][nc])


# # 전치 행렬

# arr = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]

# for i in range(3):
#     for j in range(3):
#         if i < j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


# # 절대값의 합
# dx = [-1, 1]
# dy = [-1, 1]

# if i - dx < 0:
#     continue

# # 부분집합의 합

ex = [-7, -3, -2, 5, 8]
N = len(ex)
for i in range(1 << N):
    ex_list = []
    for j in range(N):
        if i & (1 << j):
            ex_list.append(ex[j])
    if sum(ex_list) == 0:
        print(*ex_list)


# bit = [0, 0, 0, 0]

# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(*bit)

# 비트 연산자

# print(11 | 5)


# arr = [3, 6, 7, 1, 5, 4]

# n = len(arr)

# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end = ", ")
#         print()
#     print()


# 재료 = ['계란', '치츠', '떡']

# N = 3

# for i in range(1<<N):
#     ans = ''
#     for j in range(N):
#         if i & (1<<j):
#             ans += 재료[j] + ' '
#     print(ans, '라면입니다.')


# 가장 간단하고 직관적인 검색 방법
# 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서
# 원하는 항목을 찾을 때 유용함.

# 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는
# 수행시간이 급격히 증가하여 비효율적인

# 2 가지로 나눠짐
# 1. 정렬되지 않은 경우
# 2. 정렬되어 있는 경우

# 검색 과정
# 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지
# 비교하여 찾는다.
# 키 값이 동일한 원소를 찾으면 그 원소의 인섹스를 반환한다.
# 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면
# 검색 실패

# 찾고자 하는 원소의 순서에 따라 비교호수가 결정됨
# 첫 번째 원소를 찾을 때는 1번 비교, 두 번째 원소를 찾을 때는 2번 비교
# 정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수
# 시간 복잡도: O(n)

# 구현 예

def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n:
        return i
    else:
        return -1

# 정렬되어 있는 경우

# 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정
# 자료를 순차적으로 검색하면서 키 값보다 크면 찾는 원소가 없다
# 는 것이므로 더 이상 검색하지 않고 검색을 종료한다.

# 정렬이 되어 있으므로, 검색 실패를 반환하는 경우
# 평균 비교횟수가 반으로 줄어든다
# 시간복잡도: O(n)

# 구현 예

def sequentialSearch2(a, n , key):
    i = 0
    while i < n  and a[i] < key:
        i += 1
    if i < n and a[i] == key:
        return i
    else:
        return -1

# arr = [4, 9, 11, 23, 19, 7]
#
# key = 2

# for i in range(len(arr)):
#     if key == arr[i]:
#         print(i,'에 위치하고 있음')
#         break
# else:
#      print('못찾음')

# arr = [4, 9, 11, 23, 19, 7]
# key = 10
#
# for i in range(len(arr)):
#     if key == arr[i]:
#         print(i, '에 위치하고 있음')
#         break
#     elif key < arr[i]:
#         print(i,"번째 까지만 탐색해봄")
# else:
#     print('못찾음')

# 자료의 가운데에 있는 항목의 키 값과 비교하여
# 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
# 반으로 나눠서 보는 것

# 1.자료의 중앙에 있는 원소를 고른다.
# 2. 중앙 원소의 값고 찾고자 하는 못표 값을 비교한다.
# 3.목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서
# 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로
# 검색을 수행한다.

# 찾고자 하는 값을 찾을 때까지 1~3 방법을 반복

# 구현

def binarySearch(a, key):
    start = 0
    end = len(a) - 1

    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return true # 검색 성공
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return false # 검색 실패

# 재귀함수 이용

def binarySearch(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch(a, low, middle-1, key)
        elif a[middle] < key:
            return binarySearch(a, middle+1, high - 1, key)


# 선택 정렬
# k번째로 작은 원소를 찾는 알고리즘

# 1번부터 k번까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고,
# 배열의 k번째를 반환
# k가 비교적 작을 때 유용하며, O(kn)의 수행시간을 필요로 한다.

def select(list_a, k):
    for i in range(0, k):
        minIndex = i
        for j in range(i+1, len(list_a)):
            if list_a[minIndex] > list_a[j]:
                list_a[i], list_a[minIndex] = list_a[minIndex], list_a[i]
    return list_a[k-1]

# 선택 정렬

arr = [10, 15, 2, 19, 6, 14]

def selectSort(a):
    for i in range(0, len(a)-1):
        min_a = i
        for j in range(i+1, len(a)):
            if a[min_a] > a[j]:
                min_a = j
        a[i], a[min_a] = a[min_a], a[i]



