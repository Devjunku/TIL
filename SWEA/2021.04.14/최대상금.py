import sys

sys.stdin = open('input.txt')


'''
1번 뒤바꾸는 과정을 1레벨이라하면, 마지막 n번째 레벨에 도달했을 때 등장하는 건만 고려하면 된다.
그 사이에 나오는 모든 것은 답을 구하러가는 과정일 뿐 그 안에서 답이 도출된다는 생각을 하면 안 된다.

처음에 문제에 접근했을 때, 중복된 부분을 제거하기 위해 많이 애썼다.
예를 들어 setting이라는 리스트를 만들어 새롭게 만들어진 숫자는 setting 안에 집어 넣고 새롭게 만든 숫자가 setting안에 있으면 재귀를
멈추는 식으로 진행했다. 하지만, 이건 n단계까지 못가게 만드는 함정이 되었고
재귀함수가 멈추지 못하는 불상사를 겪어야 했다.
'''

def NotOverlapping(number, n):

    length = len(number)
    n = int(n)
    now_generation = set([number])
    new_generation = set()

    '''
    n단계까지 원소를 뒤바꾸는 과정을 반복한다고 했을 때 모든 경우의 수를 전부 구하는 방법을 사용할건데
    여기서 중복된건 제외(n단계가 완료되었을 때 그 결과에서 중복된 것을 제거하는 것)
    도중에 나오는 모든 경우의 수는 n단계까지 나아가기 위한 과정일 뿐 답과는 아무런 관련이 없음(여기서 답과 연결지으려는 순간 재귀 구렁텅이 빠져버렸음..)
    그래서 그 과정으로 현재의 새대와 다음 새대만을 고려하는 것
    문제 풀이 시 스택이 사용 됨.

    아이디어:

    now_generation: 특정 단계에서 등장할 수 있는 모든 경우(중복은 제외, 처음에는 입력받은 데이터 자체)
    new_generation: now_generation에서 뒤바꾸는 과정을 했을 때 나오는 모든 경우(이 역시 중복 제외)

    이러한 과정을 1번 했을 때 이 2개를 SWAP!!
    
    즉, 현재 새대는 다음 세대로 전이 되고 또 그 다음 세대로 전이
    '''

    for _ in range(n):
        while now_generation:
            level = now_generation.pop()
            level = list(level)
            for i in range(length):
                for j in range(i+1, length):
                    level[i], level[j] = level[j], level[i]
                    new_generation.add(''.join(level))
                    level[i], level[j] = level[j], level[i]
        now_generation, new_generation = new_generation, now_generation
    
    return now_generation


T = int(input())

for t in range(1, T+1):
    number, n = input().split()
    '''
    마지막 새대 중 가장 큰 값을 도출
    '''
    print(f'#{t} {max(map(int, NotOverlapping(number, n)))}')




    


