from math import factorial as f

def solution(n):
    i = 0
    while f(i) <= n:
        i += 1
        answer = i
    return answer - 1