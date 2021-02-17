# 문제 설명
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# array의 길이는 1 이상 100 이하입니다.
# array의 각 원소는 1 이상 100 이하입니다.
# commands의 길이는 1 이상 50 이하입니다.
# commands의 각 원소는 길이가 3입니다.
# 입출력 예
# array: [1, 5, 2, 6, 3, 7, 4]	
# commands: [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# return: [5, 6, 3]
# 입출력 예 설명
# [1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
# [1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
# [1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

# 내 풀이
def solution(array, commands):   
    m_list = []
    for command in commands:
        array_1 = sorted(array[(command[0]-1):(command[1])])
        m_list.append(array_1[command[2]-1])
    return m_list

# 많이 쉽게 푼 단 2줄의 다른 풀이

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# lambda를 사용해서 x를 commands로 사용하고 정렬까지 하여 return을 출력.
# 사실 array ~~~ 부터 는 내가 for 구문을 사용한 것과 같은 이치임.
# map을 사용하여 lambda 수식을 사용할 수 있게 조정.
# 마지막으로 출력의 형태는 list이기 때문에 list를 붙여줌.
# 엄청 간단한 코드

# 그 다음으로 읽기 편한 풀이

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

    # 나는 i, j, k를 활용하지 않았는데, 개인적으로 이 코드는 문제의 조건을 잘 반영하여
    # 가독성이 좋다고 느껴지는 코드 나머지는 동일
