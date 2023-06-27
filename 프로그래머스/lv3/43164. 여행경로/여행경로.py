def solution(tickets):
    
    def dfs(departure: str, path: list):
        if len(path) == n + 1:
            return path
        
        if airports.get(departure):
            for entrance in airports.get(departure):
                if visited[departure][entrance] == 0:
                    continue

                visited[departure][entrance] -= 1
                new_path = path + [entrance]
                result = dfs(entrance, new_path)
                if result:
                    return result
                visited[departure][entrance] += 1


    n = len(tickets)
    tickets.sort(key = lambda x:x[1])
    answer = []
    airports = dict()
    visited = dict()
    
    for departure, entrance in tickets:
        if airports.get(departure):
            airports[departure].append(entrance)
        else:
            airports.setdefault(departure, [entrance])
    
    for departure, entrances in airports.items():
        for entrance in entrances:
            if visited.get(departure):
                if visited[departure].get(entrance):
                    visited[departure][entrance] += 1
                else:
                    visited[departure][entrance] = 1
            else:
                visited.setdefault(departure, {entrance: 1})

    answer = dfs("ICN", ["ICN"])
    return answer