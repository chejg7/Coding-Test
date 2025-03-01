import math

def solution(a, b):
    # for i in range(2, b):
    #     if a % i == 0 and b % i == 0:
    #         a /= i
    #         b /= i
    # 이 코드의 문제점 : 동일한 수로 여러 번 나누어지는 경우를 포함하지 않음
    gcd = math.gcd(a, b)
    a /= gcd
    b /= gcd
    
    while b % 2 == 0:
        b /= 2
    while b % 5 == 0:
        b /= 5
    
    answer = 1 if b == 1 else 2
        
    return answer