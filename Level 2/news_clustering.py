# [1차] 뉴스 클러스터링

from string import ascii_lowercase

# 리스트 만들기
def make_alpha_set(string):
    
    string_set = []
    alpha_set = []
    
    for index in range(len(string) - 1):
        string_set.append(string[index] + string[index + 1])
        
    for index in string_set:
        if index[0] in ascii_lowercase and index[1] in ascii_lowercase:
            alpha_set.append(index)
    
    return alpha_set

# 교집합 개수
def check_intersection(list1, list2):
    
    count = 0
    
    for index in list1:
        if index in list2:
            count += 1
            list2.pop(list2.index(index))
            
    return count

# 합집합 개수
def check_union(list1, list2):
    
    count = 0
    
    for index in list1:
        if index in list2:
            list2.remove(index)
            
    count = len(list1) + len(list2)
    
    return count

def solution(str1, str2):
    
    # 소문자화
    str1_lower = str1.lower()
    str2_lower = str2.lower()
    
    # 리스트 만들기
    str1_list = make_alpha_set(str1_lower)
    str2_list = make_alpha_set(str2_lower)
    
    # 리스트 복사
    str1_list_copy = str1_list.copy()
    str2_list_copy = str2_list.copy()
    
    # 교집합, 합집합 후 개수 구하기
    inter_count = check_intersection(str1_list, str2_list)
    union_count = check_union(str1_list_copy, str2_list_copy)
    
    # 결과 도출
    if inter_count == 0 and union_count == 0:
        answer = 1
    else:
        answer = inter_count / union_count
        
    return int(answer * 65536)

print(solution("France", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C*2", "e=m*c^2"))
