def solution(my_string):
    answer = ''
    l = 'abcdefghijklmnopqrstuvwxyz'
    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for s in my_string:
        if s in l:
            answer += u[l.index(s)]
        else:
            answer += l[u.index(s)]
    return answer