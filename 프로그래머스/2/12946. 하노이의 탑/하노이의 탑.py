def solution(n):
    answer = []
    def hanoi(n, start, end, via):
        if n == 1:
            answer.append([start, end])
            return
        hanoi(n - 1, start, via, end)
        hanoi(1, start, end, via)
        hanoi(n - 1, via, end, start)
    hanoi(n, 1, 3, 2)
    return answer