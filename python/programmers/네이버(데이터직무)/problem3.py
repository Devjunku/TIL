'''
letters를 인덱스로 만든 후 뒤부터 뽑아야할 최소 갯수를 제외한 나머지 원소 중 가장 큰 값을 갖는 인덱스 설정, k는 1감소
이후 해당 인덱스보다 1큰 값부터 같은 행위를 반복 입력 k값이 0이면 되면 더이상 뽑을 수 없으므로 중지
사전 상 가장 뒤에 나와야하는 문자를 결정해야 함. 해당 코드의 시간복잡도는 최대 O(n*k)가 나옴
'''

def solution(letters, k):
    num_letter = []
    for letter in letters:
        num_letter.append(ord(letter))
    
    N = len(letters)
    answer = []
    start = 0

    while k > 0:
        end = N - k + 1
        idx = num_letter[start:end].index(max(num_letter[start:end]))
        start += idx + 1
        answer.append(chr(num_letter[start-1]))
        k -= 1

    return ''.join(answer)


if __name__ == '__main__':
    print(solution("zbgaj", 3))
    print(solution("zbgajzbgajzbgajzbgajzbgajzbgajzbgaj", 8))