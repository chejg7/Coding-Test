def solution(n):
    answer = sum([i for i in range(n + 1) if i % 2 == 0])
    return answer