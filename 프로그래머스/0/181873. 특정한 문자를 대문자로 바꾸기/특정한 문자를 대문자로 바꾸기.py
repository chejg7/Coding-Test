def solution(my_string, alp):
    answer = ''.join([s.upper() if s == alp else s for s in my_string])
    return answer