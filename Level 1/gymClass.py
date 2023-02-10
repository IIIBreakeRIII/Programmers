def solution(n, lost, reserve):
    answer = 0
    #지금 수업 들을 수 있는 애들
    answer = n - len(lost)

    #1번
    #체육복 여벌 있는데 잃어버린 애들
    #lost와 reserve의 배열을 비교하고 같은게 있으면 answer++, reserve배열에서 삭제
    remove_list1 = []
    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
            remove_list1.append(i)
    for i in remove_list1:
        lost.remove(i)


    #2번
    #한명한테서만 받아갈 수 있는 경우
    remove_list = []
    for i in lost:
        if not (i-1 in reserve and i+1 in reserve):
            if i-1 in reserve:
                remove_list.append(i)
                reserve.remove(i-1)
                answer += 1
            elif i+1 in reserve:
                remove_list.append(i)
                reserve.remove(i+1)
                answer += 1
    
    for i in remove_list:
        lost.remove(i)

    #3번
    #나머지
    for i in lost:
        if i-1 in reserve:
            answer += 1
        elif i+1 in reserve:
            answer += 1

    return answer

solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])
solution(3, [1,2], [2,3])