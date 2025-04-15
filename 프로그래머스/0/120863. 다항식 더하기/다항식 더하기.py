def solution(polynomial):
    p_list = polynomial.split(' + ')
    s, n = 0, 0
    
    for p in p_list:
        if 'x' in p and len(p) > 1:
            s += int(p[:-1])
        elif 'x' in p and len(p) == 1:
            s += 1
        else:
            n += int(p)
    
    s = str(s) + 'x' if s > 1 else 'x' if s == 1 else ''
    n = ' + ' + str(n) if s != '' and n > 0 else str(n) if s == '' and n > 0 else ''
    
    return s + n