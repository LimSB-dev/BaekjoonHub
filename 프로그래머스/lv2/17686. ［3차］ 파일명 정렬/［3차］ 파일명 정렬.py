def solution(files):
    n = len(files)
    file_list = []
    
    for file in files:
        file_dict = {
            "HEAD": "",
            "NUMBER": "",
            "TAIL": "",
        }
        for i in file:
            # HEAD 채우기
            # NUMBER가 채워지지 않고 숫자가 아닐 경우
            if file_dict.get("NUMBER") == "" and not i.isdigit():
                file_dict["HEAD"] += i
            # NUMBER 채우기
            # TAIL이 채워지지 않고 숫자일 경우
            elif file_dict.get("TAIL") == "" and i.isdigit():
                file_dict["NUMBER"] += i
            # TAIL 채우기
            # NUMBER가 채워져 있고 숫자가 아닐 경우
            elif file_dict.get("NUMBER") != "" and not i.isdigit():
                file_dict["TAIL"] += i
            # TAIL이 채워져 있고 숫자인 경우
            elif file_dict.get("TAIL") != "" and i.isdigit():
                file_dict["TAIL"] += i
                
        file_list.append(file_dict)

    sorted_file_list = sorted(file_list, key = lambda x: (x["HEAD"].lower(), int(x['NUMBER'])))
    answer = [f"{item['HEAD']}{item['NUMBER']}{item['TAIL']}" for item in sorted_file_list]
    return answer