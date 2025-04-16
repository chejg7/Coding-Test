def solution(my_string):
    answer = 0
    temp = '0'
    for s in my_string:
        if s in '0123456789':
            temp += s
        else:
            answer += int(temp)
            temp = '0'
    return answer + int(temp)