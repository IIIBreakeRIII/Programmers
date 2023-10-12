# 기능 개발

def develop_days(progress, speed):
    if (100 - progress) % speed == 0:
        return (100 - progress) // speed
    else:
        return ((100 - progress) // speed) + 1

def solution(progresses, speeds):
    answer = []
    until_develop = []
    max = 0
    count = 0

    for i in range(len(progresses)):
        until_develop.append(develop_days(progresses[i], speeds[i]))

    for i in range(len(until_develop)):
        if i == 0:
            max = until_develop[i]
            count += 1
            continue

        if max >= until_develop[i]:
            count += 1
            
            if i == len(until_develop) - 1:
                answer.append(count)
                break

        else:
            answer.append(count)
            max = until_develop[i]
            count = 1

            if i == len(until_develop) - 1:
                answer.append(count)
                break

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
