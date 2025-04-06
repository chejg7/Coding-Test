def solution(s):
    answer = {}
    for i in s:
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1
    
    return ''.join(sorted([key for key, val in answer.items() if val == 1]))