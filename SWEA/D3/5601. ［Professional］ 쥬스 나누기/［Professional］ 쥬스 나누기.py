for tc in range(1, int(input()) + 1):
    n = int(input())
    answer_list = [f"1/{n}" for _ in range(n)]
    answer = ' '.join(answer_list)
    
    print(f"#{tc} {answer}")