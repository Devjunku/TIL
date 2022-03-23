# x = int(input())

# if x == 64:
#     print(1)
# else:
#     stick = [64]
#     while True:

#         number = stick.pop()

#         number >>= 1
#         stick.append(number)

#         if sum(stick) > x:
#             continue
#         elif sum(stick) == x:
#             break
#         else:
#             stick.append(number)
    
# for s in stick:
#     print(x & s)

x = int(input())
cnt = 0
for i in range(6, -1, -1):
    if x & 1 << i:
        cnt += 1

print(cnt)