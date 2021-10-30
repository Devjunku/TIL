def solution(numbers):
    
    oneToNine = [i for i in range(10)]
    for number in numbers:
        oneToNine[number] = 0

    return sum(oneToNine)

if __name__ == "__main__":
    print(solution([1,2,3,4,6,7,8,0]))
    print(solution([5,8,4,0,6,7,9]))