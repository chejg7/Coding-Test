def solution(arr, delete_list):
    answer = [el for el in arr if el not in delete_list]
    return answer