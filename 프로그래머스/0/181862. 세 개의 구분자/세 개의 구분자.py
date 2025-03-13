def solution(myStr):
    answer = []
    temp = ""
    for s in myStr:
        if s == "a" or s == "b" or s == "c":
            if len(temp) > 0:
                answer.append(temp)
                temp = ""
            else:
                continue
        else:
            temp += s
    if len(temp) > 0:
        answer.append(temp)
    return answer if len(answer) > 0 else ["EMPTY"]