import sys
input = sys.stdin.readline

n = int(input())
r = int(input())
info = list(map(int, input().split()))

r_num = [0 for _ in range(102)]
r_time = [0 for _ in range(102)]
c_list = set()


for i in range(r):
    if len(c_list) < n:
        c_list.add(info[i])
        r_time[info[i]] = i
        r_num[info[i]] += 1
    elif info[i] in c_list:
        r_time[info[i]] = i
        r_num[info[i]] += 1
    else:
        # 가장 먼저 추천된 후보 찾기
        idx = 102
        long_time = 102
        for s in c_list:
            if r_time[s] < long_time:
                long_time = r_time[s]
                idx = s

        r_time[idx] = 0
        r_num[idx] = 0

        c_list.discard(idx)

        c_list.add(info[i])
        r_time[info[i]] = i
        r_num[info[i]] += 1

c_list = list(c_list)
c_list.sort()
for c in c_list:
    print(c, end=" ")