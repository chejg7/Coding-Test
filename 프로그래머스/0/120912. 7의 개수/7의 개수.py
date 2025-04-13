def solution(array):
    answer = ''.join([str(a) for a in array]).count('7')
    return answer