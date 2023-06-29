def solution(record):
    n = len(record)
    answer = []
    name_dict = dict()
    printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    def add_user(action, uid, name = "홍길동"):
        if action in ["Enter", "Change"]:
            name_dict[uid] = name


    def add_chat(action, uid, name = "홍길동"):
        if action != "Change":
            answer.append(f"{name_dict[uid]}{printer[action]}")


    for i in range(n):
        arr = record[i].split()
        add_user(*arr)
    
    for i in range(n):
        arr = record[i].split()
        add_chat(*arr)

    return answer