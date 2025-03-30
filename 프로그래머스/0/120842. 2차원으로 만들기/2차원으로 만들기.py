def solution(num_list, n):
    answer = [[]]
    i = 0
    for j, num in enumerate(num_list):
        answer[i].append(num)
        if j < len(num_list) - 1 and len(answer[i]) == n:
            i += 1
            answer.append([])
    return answer