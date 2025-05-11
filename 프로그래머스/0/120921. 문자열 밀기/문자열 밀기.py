def solution(A, B):
    answer = 0
    for i in range(len(A)):
        a = A[-i:] + A[:-i] if i > 0 else A
        if a == B:
            return i
    return -1