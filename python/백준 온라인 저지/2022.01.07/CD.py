import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    n_list = []
    m_list = []

    for _ in range(n):
        n_list.append(int(input()))

    for _ in range(m):
        m_list.append(int(input()))


    left = 0
    right = 0
    cnt = 0
    while left < n and right < m:
        if n_list[left] == m_list[right]:
            cnt += 1
            left += 1
            right += 1
        elif n_list[left] < m_list[right]:
            left += 1
        else:
            right += 1

    print(cnt)
