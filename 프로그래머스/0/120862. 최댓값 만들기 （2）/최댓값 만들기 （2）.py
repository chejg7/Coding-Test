def solution(numbers):
    numbers.sort()
    print(numbers)
    answer = max(numbers[-1] * numbers[-2], numbers[0] * numbers[1])
    return answer