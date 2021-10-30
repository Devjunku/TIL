def solution(s):
    answer = []
    for e in s:
        cnt = 0
        string = list(e)
        stack = []
        for zo in string:
            stack.append(zo) 
            if len(stack) >= 3:
                if "".join(stack[-3:]) == "110":
                    cnt += 1
                    del stack[-3:]
        idx = -1 # 0이 있는 지표
        for i in range(len(stack)):
            if stack[i] == "0":
                idx = i
        if idx < 0: ans = "110"*cnt + "".join(stack)
        else: ans = "".join(stack[:idx+1]) + (cnt * "110") + "".join(stack[idx+1:])
        answer.append(ans)
    return answer

if '__main__' == __name__:
    print(solution(["1110","100111100","0111111010"]))
    