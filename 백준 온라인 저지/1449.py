# from sys import stdin

# N, L= map(int, stdin.readline().rstrip().split())

# Tape_l = sorted(list(map(int, stdin.readline().rstrip().split())))

# tap = [0]*(max(Tape_l)+1+L)
# # print(tap)

# for l in Tape_l:
#     tap[l] = 1

# cnt = 0
# i = 0
# loca = Tape_l[0]
# while True:
#     # print(i, loca)
#     if 1 in tap[loca:loca+L]:
#         cnt += 1
#         loca += L

#     if loca > Tape_l[i]:
#         i += 1
#     else:
#         loca = Tape_l[i]
   
#     if loca > Tape_l[-1]:
#         break
# print(cnt)



m, l = map(int, input().split())
tape = list(map(int, input().split()))

tape.sort()

cnt = 0
r = 0
for i in range(m):
    if tape[i] <= r:
        continue
    cnt += 1
    r = tape[i] + (l-1)
print(cnt)

for i in range():
    

