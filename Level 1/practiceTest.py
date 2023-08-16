# 모의고사

def solution(answers):

    answer = []

    answer_temp = [0, 0, 0]

    index_1 = [1, 2, 3, 4, 5]
    index_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    index_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_list_1, answer_list_2, answer_list_3 = [], [], []

    for i in range(len(answers)):
        if i < len(index_1):
            answer_list_1.append(index_1[i])
        else:
            answer_list_1.append(index_1[i % 5])

        if i < len(index_2):
            answer_list_2.append(index_2[i])
        else:
            answer_list_2.append(index_2[i % 8])
        
        if i < len(index_1):
            answer_list_3.append(index_3[i])
        else:
            answer_list_3.append(index_3[i % 10])

    for i in range(len(answers)):
        if answer_list_1[i] == answers[i]:
            answer_temp[0] += 1

        if answer_list_2[i] == answers[i]:
            answer_temp[1] += 1
        
        if answer_list_3[i] == answers[i]:
            answer_temp[2] += 1
    
    max_score = max(answer_temp)

    for i in range(3):
        if answer_temp[i] == max_score:
            answer.append(i + 1)
        
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
