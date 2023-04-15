from collections import defaultdict


def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(int)
    genres_list = defaultdict(list)

    for idx, genre in enumerate(genres):
        genres_dict[genre] += plays[idx]
        genres_list[genre].append((idx, plays[idx]))

    genres_dict = sorted(genres_dict.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in genres_dict:
        genres_list[genre] = sorted(
            genres_list[genre], key=lambda x: x[1], reverse=True)
        answer.append(genres_list[genre][0][0])
        if len(genres_list[genre]) > 1:
            answer.append(genres_list[genre][1][0])

    return answer