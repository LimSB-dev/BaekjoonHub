for tc in range(1, int(input()) + 1):
    answer = ''
    arr1 = [list(input()) for _ in range(5)]
    
    max_length = 0
    
    for i in range(5):
        length = len(arr1[i])
        
        if length > max_length:
            max_length = length
    
    cnt = 0
    for row in range(5):
        while max_length - len(arr1[row]) != 0:
            arr1[row].append('')
            
    arr2 = [''.join(i) for i in zip(*arr1)]
    
    print(f'#{tc}', ''.join(arr2))
