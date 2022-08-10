def solution(nums):
    # 총 폰켓몬의 수
    total_count = len(nums)
    
    # 가져갈 수 있는 폰켓몬의 수
    take = total_count // 2
    
    # 중복되는 폰켓몬을 제거
    set_nums = set(nums)
    
    # 폰켓몬의 종류의 수
    count = len(set_nums)
    
    # 만약 폰켓몬의 종류의 수가 가져갈 수 있는 폰켓몬의 수보다 많거나 같다면
    # 가져가는 모든 폰켓몬을 모두 다른 종류로 가져갈 수 있다. 
    if count >= take:
        return take
    
    # 만약 폰켓몬의 종류가 가져갈 수 있는 폰켓몬의 수보다 적다면
    # 최대로 가져갈 수 있는 폰켓몬의 종류의 수는 폰켓몬의 종류의 수만큼 가져갈 수 있다.
    else:
        return count