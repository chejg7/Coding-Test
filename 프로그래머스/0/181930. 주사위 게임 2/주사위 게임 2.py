def solution(a, b, c):
    n1, n2, n3 = sorted([a, b, c])
    if n1 == n2 and n2 == n3:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    elif (n1 == n2 and n2 != n3) or (n1 != n2 and n2 == n3):
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        answer = a + b + c
    return answer