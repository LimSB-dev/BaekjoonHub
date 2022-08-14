# dice의 마주보는 index쌍
# index와 value가 서로 top, bottom 짝을 이룬다.
dice_pair = [5, 3, 4, 1, 2, 0]


# dice와 바닥면 주사위 값이 주어질 때
# 가장 큰 옆면과 윗면의 주사위 값을 반환하는 함수
def max_side(dice, bottom):
    # 바닥면의 index값
    bottom_index = dice.index(bottom)
    # 윗면의 index 값
    top_index = dice_pair[bottom_index]
    # 윗면의 주사위 값
    top = dice[top_index]
    side = []
    for num in range(1, 7):
        # top, bottom이 아니라면
        if num != bottom and num != top:
            side.append(num)
    return max(side), top


n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

# 각 면이 바닥일 경우 옆면의 합을 담을 리스트
answer = [0] * 7
bottom_num = 0

for i in range(1, 7):
    bottom_num += 1
    for j in range(n):
        value, top_num = max_side(dices[j], bottom_num)
        answer[i] += value
        bottom_num = top_num
    bottom_num = i
    
print(max(answer))
