p = 'is'
t = 'this is a book~!'
M = len(p)
N = len(t)

# 고지식한 알고리즘
def BruteForce(p, t):
    i = 0
    j = 0
    while j <  M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M # 검색 성공
    else:
        return -1 # 검색 실패

str1 = 'A pattern matching algorithm'


def BruteForce2(p, t):
    N = len(t)
    M = len(p)

    # 시작 위치를 컨트롤
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if t[i + j] == p[j]:
                cnt += 1
            else:
                break
        if cnt == M:
            return i
    return -1

print(BruteForce2(p, t))


# KMP Search

def computerLPS(pat, lps):
    leng = 0 # length of the previous longest prefix suffix
    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
            leng += 1
            lps[i] = leng
            i += 1
        else:
            # 일치하지 않는 경우
            if leng != 0:
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                leng = lps[leng-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증
                lps[i] = 0
                i += 1

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0]*M

    computerLPS(pat, lps)

    i = 0
    j = 0
    while i < N:
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if pat[j] == txt[i]:
            i += 1
            j += 1
        # 패턴을 찾지 못함
        elif pat[j] != txt[i]
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        # 패턴을 찾음
        if j == M:
            print("Found pattern at index"+str(i-j))

            j = lps[j-1]

