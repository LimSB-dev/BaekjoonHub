def solution(n, m, x, y, r, c, k):
    answer = ''
    dist = abs(x - r) + abs(y - c)
    k -= dist
    
    if k < 0 or k % 2 != 0:
        return "impossible"
    
    direction = {'d': 0, 'l': 0, 'r': 0, 'u': 0}
    
    if x > r:
        direction['u'] += x - r
    else:
        direction['d'] += r - x
    
    if y > c:
        direction['l'] += y - c
    else:
        direction['r'] += c - y
    
    answer += 'd' * direction['d']
    
    d = min(k // 2, n - (x + direction['d']))
    answer += 'd' * d
    direction['u'] += d
    k -= 2 * d
    
    answer += 'l' * direction['l']
    l = min(k // 2, y - direction['l'] - 1)
    answer += 'l' * l
    direction['r'] += l
    k -= 2 * l
    
    answer += 'rl' * (k // 2)
    answer += 'r' * direction['r']
    answer += 'u' * direction['u']
    
    return answer
