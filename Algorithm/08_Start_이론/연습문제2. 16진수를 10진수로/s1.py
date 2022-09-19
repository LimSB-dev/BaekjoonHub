import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    sixteen = input()
    ten = int(sixteen, 16)
    two = format(ten, 'b')

    while len(two) % 12 != 0:
        two = '0' + two

    answer = []

    while two:
        arr = two[:7]
        two = two[7:]
        answer.append(int(arr, 2))

    print(*answer)
