def solution(num_list):
    answer1 = int(''.join(str(num) for num in num_list if num % 2 == 1))
    answer2 = int(''.join(str(num) for num in num_list if num % 2 == 0))
    return answer1 + answer2