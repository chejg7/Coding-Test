# def solution(my_string):
#     answer = ''
#     upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lower = 'abcdefghijklmnopqrstuvwxyz'
#     for s in my_string:
#         if s in upper:
#             answer += lower[upper.index(s)]
#         else:
#             answer += s
#     return ''.join(sorted(answer))

# lower 메소드를 사용하면 매우 쉽게 풀 수 있음.

def solution(my_string):
    return ''.join(sorted(my_string.lower()))