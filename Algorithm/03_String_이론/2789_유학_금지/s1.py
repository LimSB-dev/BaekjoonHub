import sys
sys.stdin = open('input.txt')

words = input()
censorship = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

answer = ''

for word in words:
    if word in censorship:
        pass
    else:
        answer += word
        
print(answer)
