# def solution(myStr):
#     answer = []
#     temp = ""
#     for s in myStr:
#         if s == "a" or s == "b" or s == "c":
#             if len(temp) > 0:
#                 answer.append(temp)
#                 temp = ""
#             else:
#                 continue
#         else:
#             temp += s
#     if len(temp) > 0:
#         answer.append(temp)
#     return answer if len(answer) > 0 else ["EMPTY"]

def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']

# a, b, c를 빈칸으로 대치하고 이를 split하면 쉽게 풀 수 있음.
