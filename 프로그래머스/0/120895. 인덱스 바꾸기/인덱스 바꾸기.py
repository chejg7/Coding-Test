def solution(my_string, num1, num2):
    s_list = list(my_string)
    s_list[num1], s_list[num2] = s_list[num2], s_list[num1]
    return ''.join(s_list)