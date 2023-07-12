# 정수 내림차순으로 배치하기

def solution(n):

    num_list = list(map(str, str(n)))
    num_list.sort(reverse=True)

    answer = ''

    for i in range(len(num_list)):
        answer = answer + num_list[i]

    answer = int(answer)
    return answer

solution(118372)
