# [1차] 캐시 - 46번째 줄 예외 처리 안됨

def solution(cacheSize, cities):

    if cacheSize == 0:
        return len(cities) * 5
    
    cache_hit = 1
    cache_miss = 5
    pointer = 0
    answer = 0

    cache = ["NULL" for _ in range(cacheSize)]

    for i in cities:
        city = i.lower()
        if city not in cache:
            cache[pointer] = city
            answer += cache_miss
            pointer += 1
            
            if pointer == cacheSize:
                pointer = 0

        else:
            answer += cache_hit
            pointer = cache.index(city)
            pointer += 1
            
            if pointer == cacheSize:
                pointer = 0

        print(cache)

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
