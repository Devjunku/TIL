import sys

sys.stdin = open('test_input.txt')

for t in range(1, 11):

    N = int(input())

    pattern = input()
    string = input()

    P = len(pattern)
    S = len(string)
    cnt = 0
    for i in range(S-P+1):
        if pattern == string[i:i+P]:
           cnt += 1
    print(cnt)