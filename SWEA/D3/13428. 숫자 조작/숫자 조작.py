# 최소값 찾기
def min_val(n):
    li = list(n)
    for i in range(len(li)-1):
        min_idx = i
        for j in range(i + 1, len(li)):
            if li[i] > li[j]:
                if i != 0:
                    if li[min_idx] >= li[j]:
                        min_idx = j
                else:
                    if li[min_idx] >= li[j] and li[j] != '0':
                        min_idx = j

        if i != min_idx and li[i] != li[min_idx]:
            li[i], li[min_idx] = li[min_idx], li[i]
            return ''.join(li)
        
    return ''.join(li)

# 최대값 찾기
def max_val(n):
    li = list(n)
    for i in range(len(li)-1):
        max_idx = i
        for j in range(i + 1, len(li)):
            if li[i] < li[j]:
                if li[max_idx] <= li[j]:
                    max_idx = j

        if i != max_idx and li[i] != li[max_idx]:
            li[i], li[max_idx] = li[max_idx], li[i]
            return ''.join(li)

    return ''.join(li)

t = int(input())
for tc in range(1, t+1):
    n = input()
    minV = min_val(n)
    maxV = max_val(n)
    print(f"#{tc} {minV} {maxV}")