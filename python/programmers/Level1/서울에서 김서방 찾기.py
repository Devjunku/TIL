# 문제 설명
# String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요. seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# 제한 사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# Kim은 반드시 seoul 안에 포함되어 있습니다.

def solution(seoul):
    
    for i in range(len(seoul)): # 리스트 돌면서
        if seoul[i] == 'Kim': # 'Kim' 찾기
            return f'김서방은 {i}에 있다' # 찾으면 바로 '김서방은 {i}에 있다' 출력!


# 조금 더 쉽게 하려면

def solution(seoul):

    return f"김서방은 {seoul.index('kim')}에 있다"

# 로 할 수 있음.

# index() 리스트에서 원소에 해당되는 index를 알려주는 함수!!