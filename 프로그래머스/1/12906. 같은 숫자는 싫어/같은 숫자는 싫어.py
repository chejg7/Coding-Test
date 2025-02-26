def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for el in arr:
        if answer == [] or el != answer[-1]:
            answer.append(el)
    return answer