words = input()
censorship = 'CAMBRIDGE'

for alpha in censorship:
    words = words.replace(alpha, '')

print(words)