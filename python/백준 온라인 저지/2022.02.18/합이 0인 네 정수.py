import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
new_arr = []
for e in zip(*(ele for ele in arr)):
    sort_e = sorted(e)
    new_arr.append(sort_e)

a_b_dict = {}
count = 0

for a in new_arr[0]:
    for b in new_arr[1]:
        a_b_dict[a+b] = a_b_dict.get(a+b, 0) +1

for c in new_arr[2]:
    for d in new_arr[3]:
        count += a_b_dict.get(-(c+d), 0)

print(count)