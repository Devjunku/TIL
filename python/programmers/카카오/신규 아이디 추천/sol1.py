def solution(new_id):
    # 1단게
    new_id = new_id.lower()

    # 2단계
    ans = ''
    for s in new_id:
        if s.isalnum() or s in '-_.':
            ans += s
    
    # 3 단계
    while '..' in ans:
        ans = ans.replace('..', '.')
    
    # 4단계
    ans = ans[1:] if ans[0] == '.' and len(ans) > 1 else ans
    ans = ans[:-1] if ans[-1] == '.' else ans

    # 5단계
    ans = 'a' if ans == '' else ans

    # 6단계
    if len(ans) >= 16:
        ans = ans[:15]
        if ans[-1] == '.':
            ans = ans[:-1]
    
    # 7단계
    if len(ans) <= 2:
        ans = ans + ans[-1] * (3-len(ans))

    return ans



if __name__ == '__main__':
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))