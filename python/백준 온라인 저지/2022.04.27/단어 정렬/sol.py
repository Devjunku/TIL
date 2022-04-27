import sys
input = sys.stdin.readline

n = int(input())

words = set()
for _ in range(n):
    word = input().strip()
    words.add((len(word), word))
    
words = list(words)
words.sort(key=lambda x: (x[0], x[1]))

for word in words:
    print(word[1])