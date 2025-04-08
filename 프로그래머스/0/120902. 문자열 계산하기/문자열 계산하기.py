def solution(my_string):
    s_list = my_string.split(' ')
    answer = 0
    i = 0
    while i < len(s_list):
        if s_list[i] == '-':
            i += 1
            answer -= int(s_list[i])
        elif s_list[i] == '+':
            i += 1
            answer += int(s_list[i])
        else:
            answer += int(s_list[i])
        i += 1
    return answer