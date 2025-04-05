# def solution(array, n):
#     minus = [(n - i) ** 2 for i in array]
#     return array[minus.index(min(minus))]

def solution(array, n):
    answer = array[0]
    for i in array:
        if abs(n - i) < abs(n - answer):
            answer = i
        elif abs(n - i) == abs(n - answer):
            answer = min(i, answer)
    return answer
        