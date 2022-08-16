import sys
sys.stdin = open('input.txt')

left_hand, right_hand = input().split('0')

left_cnt = 0
right_cnt = 0

for hand in left_hand:
    if hand == '@':
        left_cnt += 1

for hand in right_hand:
    if hand == '@':
        right_cnt += 1

print(left_cnt, right_cnt)
