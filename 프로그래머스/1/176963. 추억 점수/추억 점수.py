def solution(name, yearning, photo):
    answer = [0 for i in range(len(photo))]
    name_yearning = {}
    for i in range(len(name)):
        name_yearning[name[i]] = yearning[i]
    for i in range(len(photo)):
        for n in photo[i]:
            if n in name_yearning:
                answer[i] += name_yearning[n]
    return answer