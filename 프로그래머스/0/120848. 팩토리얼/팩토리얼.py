# from math import factorial as f

# def solution(n):
#     i = 0
#     while f(i) <= n:
#         i += 1
#         answer = i
#     return answer - 1

# math 함수를 임포트하지 않고 팩토리얼 본연의 의미도 살리고 계산 횟수도 줄일 수 있음. 

def solution(n):
    answer = 1
    factorial = 1
    while factorial <= n:
        answer += 1
        factorial = factorial * answer
    return answer - 1
