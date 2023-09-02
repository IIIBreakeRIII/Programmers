# 구명 보트

def solution(people, limit):
    
    people.sort()
    weight_limit = limit
    boat_limit = 1
    boat_count = 1
    index = 0

    while index != len(people):
        if index + 1 == len(people):
            break

        weight_limit -= people[index]
        if weight_limit >= people[index + 1]:
            if boat_limit == 0:
                weight_limit = limit
                boat_limit = 1
                index += 1
                boat_count += 1
            else:
                index += 1
                boat_limit -= 1
        else:
            weight_limit = limit
            boat_limit = 1
            boat_count += 1
            index += 1
        
    return boat_count

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([1, 1, 1], 100))
print(solution([30, 30, 60], 160))
print(solution([10, 50, 100], 160))
print(solution([40, 40, 40, 40], 160))
print(solution([10, 10, 10, 10, 10], 150))
print(solution([30, 40, 50, 60], 100))
