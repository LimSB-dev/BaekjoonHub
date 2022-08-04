t = int(input())
answers = []
primes = [2]

# A의 범위 10^7까지의 모든 소수
for i in range(3, int(10000000 ** (0.5)), 2):
    for prime in primes:
        if not i % prime:
            break
    else:
        primes.append(i)

for tc in range(1, t + 1):
    n = int(input())
    answer = 1
    if n**0.5 != int(n**0.5):
        for prime in primes:
            cnt = 0
            while not n % prime:
                n //= prime
                cnt += 1
            if cnt % 2:
                answer *= prime
            if n == 1 or prime > n:
                break
        if n > 1:
            answer *= n
    answers.append(f'#{tc} {answer}')

for answer in answers:
    print(answer)
