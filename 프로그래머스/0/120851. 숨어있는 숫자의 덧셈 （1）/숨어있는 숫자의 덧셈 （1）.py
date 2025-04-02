def solution(my_string):
    answer = sum(int(s) for s in my_string if s.isdigit())
    return answer