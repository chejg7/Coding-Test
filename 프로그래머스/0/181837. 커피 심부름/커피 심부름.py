# def solution(order):
#     answer = 0
#     for o in order:
#         if o[:9] == "americano" or o[3:] == "americano" or o == "anything":
#             answer += 4500
#         else:
#             answer += 5000
#     return answer

# 조건식을 훨씬 간단하게 쓸 수 있음

def solution(order):
    answer = 0
    for want in order:
        if 'latte' in want:
            answer += 500
        answer += 4500

    return answer
