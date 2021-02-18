import sys

sys.stdin = open('s_input.txt', encoding='utf-8')

T = int(input())

radius_list = [20, 40, 60, 80, 100,
               120, 140, 160, 180, 200]

for t in range(1, T+1):
    N = int(input())
    score = 0
    for n in range(N):
        x, y = map(int, input().split())
        dist = (x**2 + y**2)**(0.5)
        for i in range(1, len(radius_list)):
            if radius_list[i-1] <= dist <= radius_list[i]:
                if (radius_list[i-1] - dist) >= (radius_list[i] - dist):
                    score += (200 - radius_list[i])//20
                    break
                else:
                    score += (200 - radius_list[i-1])//20
                    break
    print('#{} {}'.format(t, score))


