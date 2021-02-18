import sys

sys.stdin = open('input.txt')

for _ in range(1, 11):
    t = int(input())

    ladder_arr = []
    for i in range(100):
        zero = [0]
        arr = list(map(int, input().split()))
        zero.extend(arr)
        zero.append(0)
        ladder_arr.append(zero)

    for i in range(len(ladder_arr[0])):
        if ladder_arr[0][i]:
            target = i
            x, y = 0, i
            while True:

                # 밑
                if ladder_arr[x][y-1] == 0 and ladder_arr[x][y+1] == 0:
                    x += 1

                # 왼쪽
                if ladder_arr[x][y-1] == 1 and ladder_arr[x][y+1] == 0:
                    y -= 1
                    while ladder_arr[x][y-1]:
                        y -= 1
                        if ladder_arr[x+1][y]:
                            x += 1

                # 오른쪽
                if ladder_arr[x][y-1] == 0 and ladder_arr[x][y+1] == 1:
                    while ladder_arr[x][y+1]:
                        y += 1
                        if ladder_arr[x+1][y]:
                            x += 1

                # 종료 조건
                if x == 99:
                    break

            if ladder_arr[x][y] != 0 and ladder_arr[x][y] != 1:
                print('#{} {}'.format(t, target-1))
                break



















