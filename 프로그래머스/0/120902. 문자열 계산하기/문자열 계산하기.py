# def solution(my_string):
#     s_list = my_string.split(' ')
#     answer = 0
#     i = 0
#     while i < len(s_list):
#         if s_list[i] == '-':
#             i += 1
#             answer -= int(s_list[i])
#         elif s_list[i] == '+':
#             i += 1
#             answer += int(s_list[i])
#         else:
#             answer += int(s_list[i])
#         i += 1
#     return answer

# replace 함수를 사용해서 음수로 변환한뒤 모두 더하는 방법을 사용하면 가장 깔끔하게 풀 수 있음.
# eval()함수를 사용하는 사람도 있었으나 이는 문자열로 된 코드를 곧바로 실행해버리기 때문에 보안상 매우 위험한 행동임. 

def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))