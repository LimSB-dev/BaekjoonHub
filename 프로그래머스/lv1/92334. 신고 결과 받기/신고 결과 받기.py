def solution(id_list, report, k):
    answer = []
    
    # id별 mail 받을 횟수
    id_dict = {}
    for i in id_list:
        id_dict.setdefault(i, 0)
            
    # 신고 받은 횟수
    report_count_dict = id_dict.copy()
    
    # 신고자, 신고받은 사람
    report_person_dict = {}
    
    # 중복 신고 삭제
    report = list(set(report))
    for i in report:
        reporter, reported = i.split()
        report_count_dict[f'{reported}'] += 1
        if report_person_dict.get(f'{reporter}'):
            report_person_dict[f'{reporter}'].append(f'{reported}')
        else:
            report_person_dict.setdefault(f'{reporter}', [f'{reported}'])
    
    # 정지
    ban_list = []
    
    for key, value in report_count_dict.items():
        if value >= k:
            ban_list.append(key)
            
    for key, value in report_person_dict.items():
        for i in ban_list:
            if i in value:
                id_dict[key] += 1
    
    for value in id_dict.values():
        answer.append(value)
                
    return answer
