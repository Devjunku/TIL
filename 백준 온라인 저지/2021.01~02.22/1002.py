from sys import stdin
N = int(stdin.readline().rstrip())

for i in range(N):
    info = list(map(int, stdin.readline().rstrip().split()))
    distance =((info[0]-info[3])**2 + (info[1]-info[4])**2)**(0.5)
    if distance == 0 and info[2] == info[5]:
        print(-1)
    elif distance == 0:
        print(0)
    elif info[2] < info[5] and distance + info[2] == info[5]:
        print(1)
    elif info[2] > info[5] and distance + info[5] == info[2]:
        print(1)
    elif info[5] > info[2] and distance + info[2] < info[5]:
        print(0)
    elif info[5] < info[2] and distance + info[5] < info[2]:
        print(0)
    elif info[2] + info[5] < distance:
        print(0)
    elif info[2] + info[5] > distance:
        print(2)
    else:
        print(1)

# 생각보다 조건이 많았다.
# 그래도 엄청 어려운 문제는 아니었음
# 단지 문제를 푸는데 있어 조건이 많았을 뿐임