# 전화번호 목록

def solution(phone_book):
    
    phone_book.sort()
    
    for index in range(len(phone_book) - 1):
        if phone_book[index] in phone_book[index + 1][:len(phone_book[index])]:
            return False
    
    return True
