# def solution(num_list):
#     answer1 = int(''.join(str(num) for num in num_list if num % 2 == 1))
#     answer2 = int(''.join(str(num) for num in num_list if num % 2 == 0))
#     return answer1 + answer2

# 가독성을 고려하여 수정한 버전

def solution(num_list):
    odd = ''.join(str(num) for num in num_list if num % 2 == 1)
    even = ''.join(str(num) for num in num_list if num % 2 == 0)
    return int(odd) + int(even)
