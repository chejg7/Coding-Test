def solution(my_string):
    answer = ''
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    for s in my_string:
        if s in upper:
            answer += lower[upper.index(s)]
        else:
            answer += s
    return ''.join(sorted(answer))