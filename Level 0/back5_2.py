# 뒤에서 5등까지

def solution(num_list):
    num_list.sort()
    return num_list[:5]

print(solution([12, 4, 15, 46, 38, 1, 14]))
