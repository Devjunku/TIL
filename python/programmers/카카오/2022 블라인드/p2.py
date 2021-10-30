# sol!!

from math import sqrt

# 소수 판별 함수
def isprime(num):
    if num == 1:
        return False
    
    for i in range(2, int(sqrt(num))+1):
        if not num % i:
            return False
    return True


def solution(n, k):
    # 1이면 볼 필요없이 0임
    if n == 1:
        return 0
    # 진수 변환
    change_num = []
    while n // k:
        div, mod = divmod(n, k)
        n = div
        change_num.append(str(mod))

    # 마지막 원소 추가
    div, mod = divmod(n, k)
    change_num.append(str(mod))
    change_num = change_num[::-1]

    # stack 활용
    # P0, 0P0, 0P이 만족되면 0까지 스택에서 모두 버리고 해당 숫자만 포함하여 answer에 추가한다.

    stack1 = [] # 숫자를 쌓음
    stack2 = [] # 문자를 쌓고 0이 나오면 해당 문자를 join하여 정수로 변형후 stack1에 넣어줌
    for cnum in change_num:
        if cnum != "0": stack2.append(cnum)
        elif cnum == "0":
            if not stack2: continue
            else:
                stack1.append(int("".join(stack2)))
                stack2 = []

    # 마지막 원소 추가
    if stack2:
        stack1.append(int("".join(stack2)))

    # 소수 판별
    cnt = 0
    for s in stack1:
        if isprime(s): cnt += 1
    
    return cnt


if __name__ == "__main__":
    print(solution(437674, 3))
    print(solution(110011, 10))