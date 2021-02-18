import sys

sys.stdin = open('input.txt')

N = int(input())
Light = list(map(int, input().split()))

num = int(input())

sex = []
card = []
for _ in range(num):
    s, c = map(int, input().split())
    sex.append(s)
    card.append(c)

chan = []
for i in range(len(sex)):
    mul = []
    # 남자일때
    if sex[i] == 1:
        idx = 1
        while True:
            mul.append(card[i]*idx-1)
            idx += 1
            if card[i]*idx > N:
                break
    else: # 여자일때
        k = 1
        mul.append(card[i]-1)
        while True:
            if card[i]+k-1 <= N-1 and card[i]-k-1 >= 0 and Light[card[i]-k-1] == Light[card[i]+k-1]:
                mul.append(card[i] - k -1)
                mul.append(card[i] + k -1)
                k += 1
            else:
                break
    # print(mul)
    for i in range(len(mul)):
        if Light[mul[i]]:
            Light[mul[i]] = 0
        else:
            Light[mul[i]] = 1

for i, v in enumerate(Light):
    if i and not (i % 20):
        print()
    print(v, end = ' ')


# i = 0
# res = ''
# while i < len(Light):
#     res += str(Light[i]) + ' '
#     i += 1
#     if len(res) == 20 or i == len(Light):
#         print(res[0:len(res)-1])
#         print()
#         res = ''





