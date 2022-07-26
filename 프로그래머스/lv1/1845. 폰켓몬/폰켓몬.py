def solution(nums):
    total_count = len(nums)
    take = total_count // 2
    set_nums = set(nums)
    count = len(set_nums)
    if count >= take:
        return take
    else:
        return count