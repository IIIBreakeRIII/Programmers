# 연속 부분 수열 합의 개수

def solution(elements):

    answer_list = set(elements)
    count = 1
    front, rear = 0, 0

    while count <= len(elements):
        if front == len(elements):
            front = 0
            count += 1
        else:
            if front + count > len(elements):
                answer_list.add(sum(elements[front:front + count]) + sum(elements[rear:count - (len(elements) - front)]))
                front += 1
            else:
                answer_list.add(sum(elements[front:front + count]))
                front += 1

    answer = len(answer_list)
    return answer

print(solution([7, 9, 1, 1, 4]))
