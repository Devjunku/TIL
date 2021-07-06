'''
미리 python의 딕셔너리를 이용하여 사전을 만든 후 해당 인덱스를 추출
사전은 백트래킹으로 구현
문자는 5개이며 5 + 5**2 + 5**3 + 5**4 + 5**5까지 사전을 구성할 수 있으므로
입력값을 고려했을 때, 충분히 시간 복잡도 측면에서 구현 가능

입력을 들어오는 word 자체를 word_dic의 key값 이므로 해당 부분 바로 추출 가능
최대 시간 복잡도: O(n)
'''

word_dic = {}
idx = []
alpha = ['A', 'E', 'I', 'O', 'U']
cnt = 0
def dfs(n):
    global alpha, cnt, idx, word_dic

    if 1 <= n < 5:
        s = ''
        for i in idx:
            s += alpha[i]
        word_dic[s] = cnt    

    if n == 5:
        s = ''
        for i in idx:
            s += alpha[i]
        word_dic[s] = cnt
        return

    for i in range(5):
        idx.append(i)
        cnt += 1
        dfs(n+1)
        idx.pop()

dfs(0)

def solution(word):
    global word_dic
    return word_dic[word]

if __name__ == '__main__':
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))