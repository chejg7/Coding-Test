def solution(s):
    answer = []
    for par in s:
        if par == "(":
            answer.append(par)
        else:
            if answer and answer[-1] == "(":
                answer.pop()
            else:
                return False

    return answer == []