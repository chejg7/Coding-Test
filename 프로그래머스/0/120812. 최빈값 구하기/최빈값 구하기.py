def solution(array):
    result = {}
    for i in array:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    answer = [x for x in result.items() if x[1] == max(result.values())]
    return answer[0][0] if len(answer) == 1 else -1