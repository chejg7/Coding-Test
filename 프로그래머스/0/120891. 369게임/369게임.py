def solution(order):
    t = "369"
    answer = 0
    for s in str(order):
        if s in t:
            answer += 1
    return answer