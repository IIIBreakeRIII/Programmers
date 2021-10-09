def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    #맞힌 개수
    count = 0
    
    for num in lottos:
        if num in win_nums:
            count += 1
    
    answer.append(rank[count])
    
    for num in lottos:
        if num == 0:
            count = count + 1
            
    answer.append(rank[count])
    
    answer.sort()
            
    return answer
    #edit because of github