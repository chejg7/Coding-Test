def solution(my_str, n):
    answer = []
    i = 0
    while i < len(my_str):
        answer.append(my_str[i:i + n])
        i += n
    return answer