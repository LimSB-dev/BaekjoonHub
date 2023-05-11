def solution(name, yearning, photo):
    answer = [0] * len(photo)
    
    for index, photo_list in enumerate(photo):
        for photo_name in photo_list:
            if photo_name in name:
                jndex = name.index(photo_name)
                answer[index] += yearning[jndex]
                
    return answer