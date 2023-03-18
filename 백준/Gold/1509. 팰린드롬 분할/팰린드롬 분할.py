import sys
# sys.stdin = open('input.txt')

def is_palindrome(s):
    return s == s[::-1]

s = sys.stdin.readline().strip()
n = len(s)

dp = [0] * n
for i in range(n):
    min_cut = i + 1  # 문자열의 길이보다 큰 값을 초기값으로 설정
    for j in range(i + 1):
        if is_palindrome(s[j:i + 1]):
            if j == 0:
                # j가 0인 경우는 문자열의 시작부터 팰린드롬인 경우이므로,
                # 최소 팰린드롬 분할 개수는 1이다.
                min_cut = 1
                break
            else:
                # j가 0이 아닌 경우, j-1까지의 최소 팰린드롬 분할 개수에 1을 더한다.
                min_cut = min(min_cut, dp[j - 1] + 1)
    dp[i] = min_cut

print(dp[n - 1])