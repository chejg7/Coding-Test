# def solution(my_string):
#     answer = 0
#     temp = '0'
#     for s in my_string:
#         if s in '0123456789':
#             temp += s
#         else:
#             answer += int(temp)
#             temp = '0'
#     return answer + int(temp)

# isdigit()함수와 숫자 외의 문자를 모두 공백으로 바꿔버리는 방법을 사용하면 매우 간단하게 해결할 수 있음. 

def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())