"""
각각의 원소를 모두 mid만큼씩 나눠준다 -> 몫 + 나머지(0이상이면): 나눠준 사람의 수가 된다.
나눠준 사람의 수가 n보다 크다면,

너무 많이 나눠줬으므로,
더 많이 나눌 수 있도록 s를 높인다.

그 반대라면,
더 많은 사람에게 나눌 수 있는지 즉 mid를 줄여서 확인해본다.
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jy = [int(input()) for _ in range(m)]

s = 1
e = max(jy)
answer = 0
while s <= e:

    mid = (s + e) // 2
    num = 0

    for j in jy:
        div, mod = divmod(j, mid)
        num += div + 1 if mod > 0 else div
    
    if num > n:
        s = mid + 1
    else:
        answer = mid
        e = mid - 1

print(answer)