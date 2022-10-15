words = list(map(str, input().strip()))
words_li = []
for i in range(len(words)):
    for j in range(len(words)):
        words_li.append(''.join(words[i:j + 1]))

print(len(set(words_li)) - 1)