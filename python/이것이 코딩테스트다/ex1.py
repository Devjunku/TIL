words = input()
word_list = words.split()
long_idx = word_list[0]
idx = 0
for i in range(len(word_list)):
    if len(word_list[i]) > len(long_idx):
        long_idx = word_list[i]
        idx = i
print(word_list[idx])