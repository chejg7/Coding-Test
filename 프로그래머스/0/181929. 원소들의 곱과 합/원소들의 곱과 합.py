def solution(num_list):
    res1, res2 = 1, 0
    for num in num_list:
        res1 *= num
        res2 += num
    return int(res1 < res2 ** 2)