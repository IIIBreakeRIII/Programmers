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

def solution2(citations):

    citations.sort(reverse=True)
    print(citations)

    for idx in range(len(citations)):
        if idx >= citations[idx]:
            return idx

    return len(citations)

print(solution2([3, 0, 6, 1, 5]))
print(solution2([2, 0, 6, 1, 5]))
print(solution2([0, 0, 0, 0, 0]))
print(solution2([6, 5, 5, 5, 3, 2, 1, 0]))
