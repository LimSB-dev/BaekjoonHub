def solution(queue1, queue2):
    def sum_array(array):
        return sum(array)

    queue3 = queue1 + queue2
    target = sum(queue3) // 2

    if sum(queue3) % 2 != 0:
        return -1

    queue = queue1 + queue2 + queue1
    max_count = len(queue)

    answer, left, right, sum_value = 0, 0, len(queue1), sum(queue1)

    while answer <= max_count:
        if sum_value == target:
            return answer
        elif sum_value < target:
            sum_value += queue[right]
            right += 1
            answer += 1
        elif sum_value > target:
            sum_value -= queue[left]
            left += 1
            answer += 1

    return -1