# H-Index

def solution(citations):

    answer = []
    
    for index in citations:
        n = 0
        for j in citations:
            if index >= j:
                n += 1

        if n == index:
            answer.append(index)

    return max(answer)

print(solution([3, 0, 6, 1, 5]))
