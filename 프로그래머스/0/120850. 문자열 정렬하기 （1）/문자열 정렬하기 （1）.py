def solution(my_string):
    answer = sorted([int(s) for s in my_string if s in "0123456789"])
            
    return answer