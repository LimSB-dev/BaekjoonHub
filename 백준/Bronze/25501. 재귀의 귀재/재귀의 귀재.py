def recursion(s, left, right):
    global cnt

    cnt += 1
    
    if left >= right:
        return 1
    elif s[left] != s[right]:
        return 0
    else:
        return recursion(s, left + 1, right - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


n = int(input())
for _ in range(n):
    words = input()
    cnt = 0

    answer = isPalindrome(words)

    print(answer, cnt)
