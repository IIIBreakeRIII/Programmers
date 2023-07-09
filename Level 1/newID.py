# 신규 아이디 추천

def solution(new_id):
    
    # 대문자 소문자 치환
    lower_new_id = new_id.lower()

    # 문자 제거
    list_new_id = list(map(str, str(lower_new_id)))

solution("...!@BaT#*..y.abcdefghijklm")
