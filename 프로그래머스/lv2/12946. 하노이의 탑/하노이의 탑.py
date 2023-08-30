def solution(n):
    def solution_(n, from_, through, to):
        if n == 1:
            return [[from_, to]]
        result = []
        result.extend(solution_(n - 1, from_, to, through))
        result.append([from_, to])
        result.extend(solution_(n - 1, through, from_, to))
        return result

    return solution_(n, 1, 2, 3)
