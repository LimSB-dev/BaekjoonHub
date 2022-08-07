t = int(input())

for tc in range(1, t + 1):
    li = list(input().split())
    robots = {'O': [1, 0], 'B': [1, 0]}
    answer = 0
    for i in range(1, len(li)-1, 2):
        name = li[i]
        button = int(li[i+1])
        distance = abs(button - robots[name][0])
        robot_sec = answer - robots[name][1]
        answer += 1 if distance <= robot_sec else (distance-robot_sec+1)
        robots[name][0] = button
        robots[name][1] = answer

    print(f'#{tc} {answer}')