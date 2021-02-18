import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    string = input()
    l = []
    # 레이저 담는 곳
    layer_list = []
    # 층 담는 곳
    i = 0
    # 인덱스 순환
    while i < len(string):
        # 인덱스가 문자열의 갯수보다 많으면 종료
        if string[i:i+2] == '()':
            # 두개를 보니 '()'인가?
            l.append([i, i+1])
            #그러면 레이저니까 l에 추가
            i += 2
            # 레이져는 2개이므로 인덱스를 2개 증가
        elif string[i] == '(':
            # 그렇지 않고 괄호는 열면
            k = i
            # k=i로 가고
            stack = 0
            # 이제부터 닫히는 부분 찾을 것임 세면서..
            stack_list = [k]
            # 일단 괄호 열렸으니까 그 부분 stack_list에 추가
            while k < len(string):
                # k가 문자열보다 크면 중단
               if string[k] == '(':
                   # 문자열의 k의 인덱스에서 '('이면
                   stack += 1 # stack에 1
               else: # 그렇지 않으면
                   stack -= 1 # stack에 -1

               if stack == 0:
                   # 여기서 stack이 0이면
                   stack_list.append(k)
                   # stack_list에 k를 추가 즉 괄호가 닫히는 부분
                   layer_list.append(stack_list)
                   # 레이저인 부분
                   break
                   # 찾았으니 브레이크
               k += 1
                # 계속 1은 더해야함
            i += 1
            # 계속 1은 더해야함
        else:
            i += 1
            # 계속 1은 더해야함

    res_cnt = 0
    # 최종계수 담는 곳
    for bound in layer_list:
        # 층별 괄호 인덱스
        cnt = 1
        # 초기값
        for laser in l:
            # 레이저 인덱스
            if bound[0] < laser[0] and laser[1] < bound[1]:
                # 층별에 레이저가 있으면
                cnt += 1
                # 1을 더함
        if cnt != 1:
            #근데 만약에 초깃값 그대로면 레이저가 짜르지 않는다는 의미이므로 1이 아닐 때만 더해야함
            res_cnt += cnt
            # 더하기

    print('#{} {}'.format(t, res_cnt))
    # 최종 결과 출력

