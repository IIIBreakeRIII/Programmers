def solution(a, b):
    Week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    Days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total_days = 0
    
    for i in range(0, a-1):
        total_days += Days[i]
    
    total_days += b - 1
    answer_days = total_days % 7
    
    answer = Week[answer_days]
    return answer
    
    solution(5, 24)