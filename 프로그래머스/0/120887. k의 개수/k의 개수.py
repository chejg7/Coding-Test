def solution(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        for p in str(n):
            if str(p) == str(k):
                answer += 1
    return answer