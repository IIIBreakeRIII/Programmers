# 가까운 1 찾기

def solution(arr, idx):
    if arr[idx] == 1:
        return idx
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1

