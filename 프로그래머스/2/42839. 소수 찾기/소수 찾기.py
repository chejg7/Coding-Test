from itertools import permutations

def solution(numbers):
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = set()
    
    for i in range(len(numbers)):
        for j in permutations(numbers, i + 1):
            num = int(''.join(j))
            if is_prime(num):
                primes.add(num)
    
    return len(primes)