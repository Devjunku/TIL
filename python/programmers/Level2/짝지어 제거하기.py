def solution(s):
    stack = []

    for sub_s in s:
        if stack:
            if stack[-1] == sub_s:
                stack.pop()
            else:
                stack.append(sub_s)
        else:
            stack.append(sub_s)
    
    if stack: return 0
    else: return 1
        
if __name__ == "__main__":
    print(solution("baabaa"))
    print(solution("cdcd"))