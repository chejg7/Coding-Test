def solution(n):
    answer = 0
    str_num = str(n)
    for s in str_num:
        answer += int(s)
    return answer