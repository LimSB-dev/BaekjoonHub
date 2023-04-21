str = input()
answer = ''
for char in str:
    if char.isupper():
        answer += char.lower()
    else:
        answer += char.upper()
print(answer)