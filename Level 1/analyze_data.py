# [PCCE 기출문제] 10번 / 데이터 분석

def criteria(ext):
    
    if ext == "code":
        return 0
    elif ext == "date":
        return 1
    elif ext == "maximum":
        return 2
    else:
        return 3

def solution(data, ext, val_ext, sort_by):
    
    except_criteria = criteria(ext)
    
    result_data = []
    
    for lst in data:
        if lst[except_criteria] <= val_ext:
            result_data.append(lst)
            
    sort_criteria = criteria(sort_by)
    
    result_data.sort(key=lambda x:x[sort_criteria])
    
    return result_data
