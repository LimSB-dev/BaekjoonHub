def solution(record):
    n = len(record)
    answer = []
    name_dict = dict()
    
    def add_user(uid, name):
        if name_dict.get(uid):
            name_dict[uid] = name
        else:
            name_dict.setdefault(uid, name)
    
    
    def add_chat(action, uid, name = "홍길동"):
        if action == "Enter":
            saved_name = name_dict.get(uid)
            if saved_name:
                answer.append(f"{saved_name}님이 들어왔습니다.")
            else:
                name_dict.setdefault(uid, name)
                answer.append(f"{name}님이 들어왔습니다.")
        elif action == "Leave":
            saved_name = name_dict.get(uid)
            if saved_name:
                answer.append(f"{saved_name}님이 나갔습니다.")
            else:
                answer.append(f"{name}님이 나갔습니다.")
        elif action == "Change":
            return
        else:
            return    
    
    for i in range(n):
        arr = record[i].split()
        if len(arr) == 3:
            add_user(arr[1], arr[2])
    
    for i in range(n):
        arr = record[i].split()
        add_chat(*arr)

    return answer