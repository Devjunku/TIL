import math, sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * n

for i in range(n):
    arr[i] = int(input())

h = int(math.ceil(math.log2(n)))
tree_size = (1 << (h + 1))
mintree = [0] * tree_size
maxtree = [0] * tree_size

def initmin(start, end, index):
    if start == end:
        mintree[index] = arr[start]
        return mintree[index]
    mid = (start + end) // 2
    mintree[index] = min(
        initmin(start, mid, index * 2),
        initmin(mid + 1, end, index * 2 + 1))

    return mintree[index]


def querymin(start, end, index, left, right):
    if left > end or right < start:
        return math.inf
    if left <= start and end <= right:
        return mintree[index]
    
    mid = (start+end) // 2

    return min(
        querymin(start, mid, index * 2, left, right),
        querymin(mid + 1, end, index * 2 + 1, left, right)
    )


def initmax(start, end, index):
    if start == end:
        maxtree[index] = arr[start]
        return maxtree[index]
    mid = (start + end) // 2
    maxtree[index] = max(
        initmax(start, mid, index*2),
        initmax(mid+1, end, index*2+1))
    return maxtree[index]


def querymax(start, end, index, left, right):
    if left > end or right < start:
        return -1
    
    if left <= start and end <= right:
        return maxtree[index]
    
    mid = (start+end) // 2
    return max(
        querymax(start, mid, index*2, left, right),
        querymax(mid+1, end, index*2 + 1, left, right)
        )


initmin(0, n-1, 1)
initmax(0, n-1, 1)

answer = ""
for i in range(m):
    s, e = map(int, input().split())
    answer += str(querymin(0, n-1, 1, s-1, e-1)) + " " + str(querymax(0, n-1, 1, s-1, e-1)) + "\n"

print(answer)

