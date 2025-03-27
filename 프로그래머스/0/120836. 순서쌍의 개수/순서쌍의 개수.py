def solution(n):
    answer = 0
    for i in range(1, n + 1):
        q = n // i
        if i * q == n:
            answer += 1
    return answer