import math

def solution(fees, records):
    answer = []
    dict_minute = {}
    dict_record = {}
    
    for record in records:
        time, num, in_out = record.split()
        hour, minute = map(int, time.split(':'))
        # 분으로 변환
        minutes = hour * 60 + minute
        
        if in_out == 'IN':
            dict_record.setdefault(num, minutes)
        else:
            # 입차 시간
            in_minutes = dict_record.get(num)
            # 누적 주차 시간(분)
            total_minutes = minutes - in_minutes
            
            # 누적 주차 시간 Dictionary 추가
            if num in dict_minute.keys():
                dict_minute[num] += total_minutes
            else:
                dict_minute.setdefault(num, total_minutes)
            
            # 입차 기록 삭제
            dict_record.pop(num)
    
    # 23:59 이후 입차 기록 미삭제
    if dict_record:
        for key, value in dict_record.items():
            # 입차 시간
            in_minutes = value
            # 출차 시간
            out_minutes = 23 * 60 + 59
            # 누적 주차 시간
            total_minutes = out_minutes - in_minutes
            # 누적 주차 시간 Dictionary 추가
            if key in dict_minute.keys():
                dict_minute[key] += total_minutes
            else:
                dict_minute.setdefault(key, total_minutes)
            
    dict_minute = sorted(dict_minute.items())
    print(dict_minute)
    
    for price in dict_minute:
        parking_fee = fees[1] + math.ceil((price[1] - fees[0] if price[1] - fees[0] > 0 else 0) / fees[2]) * fees[3]
        answer.append(parking_fee)
    return answer