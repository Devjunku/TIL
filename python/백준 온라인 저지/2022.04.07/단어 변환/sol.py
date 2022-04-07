from collections import deque

def compare_word(begin, words):
    changeword = []
    for word in words:
        cnt = 0
        for b, w in zip(list(begin), list(word)):
            if b != w:
                cnt += 1
        if cnt == 1:
            changeword.append(word)

    return changeword


def solution(begin, target, words):
    visited = {
        word: False for word in words
    }

    first = compare_word(begin, words)
    q = deque([])
    for f in first:
        visited[f] = True
        q.append((f, 1))
    
    while q:
        word, cost = q.popleft()
        if word == target:
            return cost
        compare_change = compare_word(word, words)
        for change in compare_change:
            if not visited[change]:
                visited[change] = True
                q.append((change, cost + 1))
            
    return 0
    
if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0