def solution(my_string):
    answer = ''
    for s in my_string:
        if s in "aeiou":
            continue
        answer += s
    
    return answer