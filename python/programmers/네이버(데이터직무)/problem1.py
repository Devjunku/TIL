'''
문자열을 정렬 후 인덱싱 슬라이싱으로 하나씩 비교
최대 시간 복잡도 O(n)
'''

def solution(S, pattern):

    S = list(S)
    pattern = ''.join(sorted(list(pattern)))
    Np = len(pattern)
    Ns = len(S)
    answer = 0
    for n in range(Ns-Np+1):
        s = sorted(S[n:n+Np])
        if ''.join(s) == pattern:
            answer += 1
    
    return answer


if __name__ == '__main__':
    print(solution("tegsornamwaresomran", "ransom"))
    print(solution("wreawerewa", "ware"))
    print(solution("ababababababa", "aabba"))
    print(solution("abcde", "edcba"))
    print(solution("aabbccddee", "abcde"))
    print(solution("aaaaaa", "a"))