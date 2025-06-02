from itertools import combinations as cb

def solution(number):
    answer = len([nums for nums in cb(number, 3) if sum(nums) == 0])
    return answer