def solution(num, total):
    avg = total // num
    start = avg - (num // 2)
    if num % 2 == 0:
        start += 1
    answer = [i for i in range(start, start + num)]
    return answer