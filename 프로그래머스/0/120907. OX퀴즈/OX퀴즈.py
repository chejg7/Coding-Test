def solution(quiz):
    answer = []
    for q in quiz:
        l_str, r_str = q.split(' = ')
        [a, b, c] = l_str.split(' ')
        l_num = int(a) + int(c) if b == '+' else int(a) - int(c)
        r_num = int(r_str)
        
        if l_num == r_num:
            answer.append('O')
        else:
            answer.append('X')
    return answer