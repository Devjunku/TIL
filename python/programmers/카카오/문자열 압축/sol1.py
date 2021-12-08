def solution(s):
    
    s_len = len(s)

    if s_len == 1:
        return 1

    ans = 10000

    for i in range(1, (s_len//2)+1):
        string = []
        num = 1

        for j in range(0, s_len, i):
            if not string:
                string.append(s[j:j+i])
                continue

            if s[j:j+i] == string[-1]:
                num += 1
            else:
                if num == 1:
                    string.append(s[j:j+i])
                    continue

                string[-1] = str(num) + string[-1]
                string.append(s[j:j+i])
                num = 1

        if num == 1:
            if ans > len("".join(string)):
                ans = len("".join(string))
            continue
        
        string[-1] = str(num) + string[-1]
        if ans > len("".join(string)):
            ans = len("".join(string))
    return ans
            



if __name__ == "__main__":
    print(solution("a"))
    # print(solution("aabbaccc"))
    # print(solution("ababcdcdababcdcd"))
    # print(solution("abcabcdede"))
    # print(solution("abcabcabcabcdededededede"))
    # print(solution("xababcdcdababcdcd"))