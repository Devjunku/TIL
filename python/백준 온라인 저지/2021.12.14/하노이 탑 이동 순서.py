import sys

sys.setrecursionlimit = 1000000

n = int(input())

# 2차월 배열을 만들어서 원소를 문제의 조건에 따라 넣었다 빼는게 좋은거 같다.
# 입력값이 20까지 밖에 안 되기 때문에 모든 경우를 고려해서 코드를 짜도 괜찮으므로
# 한 번 시행 할 때 마다 같은 조건으로 진행되기 때문에 재귀함수로 진행해보자.
# 물론 움직일 수 있는 장소는 정해져있기 때문에 해볼만 하다.

moving = [(0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (2, 1)]

top = [[] for _ in range(3)]
top[0] = [i for i in range(n, 0, -1)]

answer = sys.maxsize

moving_method = []


# 함수의 작동 알고리즘에서 무조건 처음에는 0번 index에서 하나의 원소를 뽑고 시작해야 한다.
# 그 원소를 first라고 하자.
# 그리고 문제의 정지 규칙은 아래와 같다.

def is_sequence_reversed(arr, n):

    n_arr = [i for i in range(n, 0, -1)]
    for c1, c2 in zip(arr, n_arr):
        if c1 != c2:
            return False

    return True


def hanoi_top(top, cnt, method):
    global answer, moving_method

    if cnt >= (2**n)-1:
        if answer > cnt:
            answer = cnt
        if is_sequence_reversed(top, n):
            moving_method = method
        return
    
    for move in moving:
        start, end = move
        if not top[start]:
            continue

        if top[end]:
            if top[start][-1] < top[end][-1]:
                top[end].append(top[start].pop())
                method.append(move)
                hanoi_top(top, cnt+1, method)
                top[start].append(top[end].pop())
                method.pop()
        else:
            top[end].append(top[start].pop())
            method.append(move)
            hanoi_top(top, cnt+1, method)
            top[start].append(top[end].pop())
            method.pop()
            

hanoi_top(top, 0, [])
print(answer)