# 구명 보트

def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    
    while a < b :
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1

        b -= 1
        
    return len(people) - answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([1, 1, 1], 100))
print(solution([30, 30, 60], 160))
print(solution([10, 50, 100], 160))
print(solution([40, 40, 40, 40], 160))
print(solution([10, 10, 10, 10, 10], 150))
print(solution([30, 40, 50, 60], 100))
