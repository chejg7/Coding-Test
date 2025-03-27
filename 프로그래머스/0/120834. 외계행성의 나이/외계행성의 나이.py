def solution(age):
    answer = ''
    num_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for s in str(age):
        answer += num_str[int(s)]
    return answer