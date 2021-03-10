def solution(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = []
        for word_1 in Q:
            if word_1 == target:
                    return answer
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                if sum([x!=y for x, y in zip(word_1, word_2)]) == 1:
                    temp_Q.append(words.pop(i))

        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1


# cnt = 0
# def dfs(begin, target, words, visited):
#     global cnt
#     stacks = [begin]

#     while stacks:
#         stack = stacks.pop()

#         if stack == target:
#             return cnt

#         for i in range(0, len(words)):
#             if len([j for j in range(len(words[i])) if stack[j] != words[i][j]]) == 1:
#                 if visited[i] != 0:
#                     continue    
#                 visited[i] = 1
#                 stacks.append(words[i])
#         cnt += 1

# def solution(begin, target, words):
#     global cnt
#     visited = [0]*len(words)

#     if target not in words:
#         return 0

#     dfs(begin, target, words, visited)

#     return cnt