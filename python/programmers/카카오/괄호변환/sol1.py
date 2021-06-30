def devide(w):
    openP = 0
    closeP = 0

    for i in range(len(w)):
        if w[i] == "(": openP += 1
        else: closeP += 1

        if openP == closeP: return w[:i+1], w[i+1:]


def is_b(u):
    stack = []

    for s in u:
        if s == "(": stack.append(s)
        else:
            if not stack: return False
            stack.pop()

    return True


def solution(w):
    if not w: return ""
    
    u, v = devide(w)

    if is_b(u): return u + solution(v)
    else:
        answer = '('
        print(v)
        answer += solution(v)
        print(answer)
        answer += ')'

        for p in u[1:len(u)-1]:
            if p == '(': answer += ')'
            else: answer += '('
        
        return answer


if __name__ == "__main__":
    print(solution("(()())()"))
    print(solution(")("))
    print(solution("()))((()"))