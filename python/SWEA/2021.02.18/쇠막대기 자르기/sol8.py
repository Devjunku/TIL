T = int(input())
for tc in range(1, T + 1):
    def cutting(bar_list):
        count = 0  # 같이 나아가는 쇠막대의 갯수
        laser = 0  # 이전이 레이저였나 판단
        result = 0  # 총 갯수
        bar = 1  # 잘리면서 두개로 나뉘므로 1 더해줘야하는 변수
        for i in range(len(bar_list)):
            if bar_list[i] == '(':
                count += 1
                laser = 0
            elif bar_list[i] == ')':
                if laser == 0:
                    laser = 1
                    count -= 1
                    result = result + count
                elif laser == 1:
                    count -= 1
                    result += bar
        return result


    bar_list = list(input())
    cutting_bar = cutting(bar_list)

    print('#{} {}'.format(tc, cutting_bar))