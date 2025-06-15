def solution(arr):
    answer = [num / 2 if num >= 50 and num % 2 == 0 else num * 2 if num < 50 and num % 2 == 1 else num for num in arr]
    return answer