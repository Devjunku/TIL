import sys
from collections import deque
sys.stdin = open("sample_input.txt")

T = int(input())

sixteen_dic = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


for t in range(1, T+1):
    n, k = map(int, input().split())
    string = deque(list(input().strip()))
    ranking = set()
    term = n//4
    for i in range(term):
        sample = "".join(list(string))
        for j in range(0, n, term):
            value = 0
            for h in range(term):
                value += (16**(term-h-1))*sixteen_dic[sample[j:j+term][h]]
            ranking.add(value)
            
        string.rotate(1)
    result = list(ranking)
    result.sort(reverse=True)
    print(f"#{t} {result[k-1]}")