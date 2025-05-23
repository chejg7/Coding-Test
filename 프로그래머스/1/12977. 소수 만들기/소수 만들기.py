from itertools import combinations as comb

def solution(nums):
    answer = 0

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = [sum(num) for num in comb(nums, 3)]
    for n in result:
        if is_prime(n):
            answer += 1

    return answer