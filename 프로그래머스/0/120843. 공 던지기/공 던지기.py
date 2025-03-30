def solution(numbers, k):
    i = 0
    while k > 1:
        i += 2
        if i > len(numbers) - 1:
            i = i - len(numbers)
        k -= 1
    return numbers[i]