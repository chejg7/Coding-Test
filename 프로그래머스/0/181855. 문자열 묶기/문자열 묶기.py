# def solution(strArr):
#     answer = {}
#     for s in strArr:
#         length = len(s)
#         if length in answer:
#             answer[length] += 1
#         else:
#             answer[length] = 1
#     return max(answer.values())

def solution(strArr):
    d = {}

    for i in strArr:
        d[len(i)] = d.get(len(i), 0) + 1

    return max(d.values())

# 딕셔너리의 get 메소드를 사용하면 더 간단하게 작성할 수 있음.