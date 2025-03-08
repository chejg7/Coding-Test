def solution(order):
    answer = 0
    for o in order:
        if o[:9] == "americano" or o[3:] == "americano" or o == "anything":
            answer += 4500
        else:
            answer += 5000
    return answer