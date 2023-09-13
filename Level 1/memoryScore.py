# 추억 점수

def solution(name, yearning, photo):

    memory_score = {}
    answer = []

    for i in range(len(name)):
        memory_score[name[i]] = yearning[i]

    for index in photo:
        score = 0
        for i in range(len(index)):
            if index[i] in memory_score:
                score += memory_score[index[i]]

        answer.append(score)

    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))
