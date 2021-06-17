from sys import stdin

N = int(stdin.readline().rstrip())

def solution(string):
    if '(' not in string or ')' not in string:
        return 'NO'
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif len(stack) > 0 and string[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'NO' 
        elif len(stack) == 0 and string[i] == ')':
            return 'NO'
    if len(stack) > 0:
        return 'NO'
    else:
        return 'YES'

for _ in range(N):
    try:
        string = stdin.readline().rstrip()
        print(solution(string))
    except:
        print('NO')
    
if __name__  == '__main__':
    print(solution(''))
    print(solution('(())())'))
    print(solution('(((()())()'))
    print(solution('(()())((()))'))
    print(solution('((()()(()))(((())))()'))
    print(solution('()()()()(()()())()'))
    print(solution('(()((())()('))
    print(solution('(('))
    print(solution('))'))
    print(solution('())(()'))
