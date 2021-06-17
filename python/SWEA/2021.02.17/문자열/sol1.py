word = 'abcde'

# 내장 함수 안쓰고
reversed_word = ''
for i in range(len(word)-1, -1, 1):
    reversed_word += word[i]

# print(reversed_word)

#
list_w = list(word)
for i in range(len(word) // 2):
    list_w[i], list_w[-i-1] = list_w[-i-1], list_w[i]

# print(''.join(list_w))

# 재귀함수
def recur_string(string, i):
    if i <= 0:
        return
    print(string[i-1], end = '')
    recur_string(string, i-1)

recur_string(word, len(word))





# print(word[0:-1])





