def solution(numbers):
    sorted_num = sorted(numbers, reverse = True)
    return sorted_num[0] * sorted_num[1]