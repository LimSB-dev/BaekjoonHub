def solution(numbers, hand):
    answer = ''
    
    left_row = 3
    left_col = 0
    
    right_row = 3
    right_col = 2
    
    # 번호 누르기
    for i in numbers:
        # 0일 경우
        if i == 0:
            # 0과 왼손 거리
            left_distance = (3 - left_row) + (1 - left_col)
            # 0과 오른손 거리
            right_distance = (3 - right_row) + (right_col - 1)
                        
            if left_distance > right_distance:
                right_row = 3
                right_col = 1
                answer += 'R'
            elif left_distance < right_distance:
                left_row = 3
                left_col = 1
                answer += 'L'
            else:
                if hand == 'right':
                    right_row = 3
                    right_col = 1
                    answer += 'R'
                else:
                    left_row = 3
                    left_col = 1
                    answer += 'L'
        # 0이 아닐 경우
        else:
            # 열 찾기
            col = i % 3
            # 오른손
            if col == 0:
                right_row = (i//3) - 1
                right_col = (i%3) - 1
                if right_col == -1:
                    right_col = 2
                answer += 'R'
            # 왼손
            elif col == 1:
                left_row = i // 3
                left_col = (i%3) - 1
                answer += 'L'
            # 중앙
            else:
                i_row = i // 3
                i_col = (i%3) - 1
                
                # 왼손 거리
                left_distance = abs(i_row - left_row) + (i_col - left_col)
                # 오른손 거리
                right_distance = abs(i_row - right_row) + (right_col - i_col)
                
                if left_distance > right_distance:
                    right_row = i_row
                    right_col = i_col
                    answer += 'R'
                elif left_distance < right_distance:
                    left_row = i_row
                    left_col = i_col
                    answer += 'L'
                else:
                    if hand == 'right':
                        right_row = i_row
                        right_col = i_col
                        answer += 'R'
                    else:
                        left_row = i_row
                        left_col = i_col
                        answer += 'L'
    return answer