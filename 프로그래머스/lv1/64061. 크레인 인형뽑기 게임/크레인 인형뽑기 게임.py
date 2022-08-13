def solution(board, moves):
    answer = 0
    grabed_box = []
    n = len(board)
    for i in moves:
        for row in range(n):
            
            # 뽑기
            if board[row][i - 1] != 0:
                grab = board[row][i - 1]
                board[row][i - 1] = 0
                
                # 바구니가 비어있지 않다면
                if grabed_box:
                    
                    # 뽑은 인형과 바구니 가장 위의 인형이 같다면
                    if grabed_box[-1] == grab:
                        answer += 2
                        
                        # 가장 위의 인형 삭제
                        grabed_box.pop()  
                    else:
                        grabed_box.append(grab)                    
                    break
                    
                # 비어 있다면
                else:
                    grabed_box.append(grab)
                    break   
    return answer