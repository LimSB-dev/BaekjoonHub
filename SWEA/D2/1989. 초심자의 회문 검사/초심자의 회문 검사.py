t = int(input())

for i in range(t):
    word = str(input())
    lenght = len(word)
    palindrome = 1
    for j in range(lenght // 2):
        if word[j] != word[(lenght - 1) - j]:
            palindrome = 0
            break
    print(f"#{i+1} {palindrome}")