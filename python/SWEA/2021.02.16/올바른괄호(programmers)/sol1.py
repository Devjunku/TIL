def solution(s):

    Queue = []
    for i in s:
        if i == '(':
            Queue.append('(')
        else:
            try:
                Queue.pop()
            except:
                return False
    if len(Queue) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(solution('()()'))
    print(solution('(())()'))
    print(solution(')()('))
    print(solution('(()('))