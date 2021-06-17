def palin(string):
    if string == string[::-1]:
        return True
    return False

def solution(s):
    n = len(s)
    for i in range(n, 0, -1):
        for j in range(n-i+1):
            if palin(s[j:j+i]):
                return i


if __name__ == '__main__':
    print(solution("abcdcba"))
    print(solution("abacde"))