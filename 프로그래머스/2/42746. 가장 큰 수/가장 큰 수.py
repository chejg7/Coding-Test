# def solution(numbers):
#     answer = ''
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             num1 = int((str(numbers[i]) * 4)[:4])
#             num2 = int((str(numbers[j]) * 4)[:4])
#             if num1 < num2:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]
#     for n in numbers:
#         answer += str(n)
#     return answer

# 버블 정렬 방식 : 중첩 루프를 사용하기 때문에 O(N^2)의 시간 복잡도를 가짐. 
# NlogN의 시간 복잡도를 가지는 파이썬의 sorted 함수를 사용하되, 키를 사용해 단순 내림차순이 아니라 붙였을 때 큰 수의 순서로 정렬되도록 함

def solution(numbers):
    numbers = sorted(numbers, key = lambda x : (str(x) * 4)[:4], reverse = True)
    answer = str(int(''.join(map(str, numbers))))
    return answer