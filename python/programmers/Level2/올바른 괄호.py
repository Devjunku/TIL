def solution(s):

    Queue = []
    for i in s:
        if i == '(': # '(' 가 무조건 먼저 나와야하는 성질을 이용하여 문제를 접근
            Queue.append('(') # '(' 이면 추가
        else: # 그렇지 않으면 
            try:
                Queue.pop() # 마지막 '(' 를 삭제
            except:
                return False # 오류가 나면 '(' 가 없이 ')'가 나왔다는 이야기이므로 틀림
    if len(Queue) == 0: #그리고 stack의 수가 0이면 균형을 맞췄다는 것이므로
        return True # True
    else:
        return False # 그렇지 않으면 False


if __name__ == '__main__':
    print(solution('()()'))
    print(solution('(())()'))
    print(solution(')()('))
    print(solution('(()('))
