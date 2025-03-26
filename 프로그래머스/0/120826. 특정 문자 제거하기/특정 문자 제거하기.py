def solution(my_string, letter):
    answer = ''
    for s in my_string:
        if s == letter:
            continue
        else:
            answer += s
    return answer