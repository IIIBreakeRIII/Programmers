# [1차] 캐시

def solution(cacheSize, cities):

    cache = []
    answer = 0

    for city in cities:
        city = city.lower()
        if cacheSize != 0:
            if city not in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                answer += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1

        else:
            answer += 5

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["a", "b", "c", "a"]))
print(solution(3, ["a", "b", "c", "a", "b"]))
print(solution(3, ["a", "b", "c", "a", "b", "d", "c"]))
print(solution(3, ["b", "c", "b", "a", "e", "b", "c", "e"]))
