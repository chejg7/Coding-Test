def solution(sizes):
    answer = [0, 0]
    for size in sizes:
        w, h = size
        if h > w:
            h, w = w, h
        if w > answer[0]:
            answer[0] = w
        if h > answer[1]:
            answer[1] = h
    
    return answer[0] * answer[1]