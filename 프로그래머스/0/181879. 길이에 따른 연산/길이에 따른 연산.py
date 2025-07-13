from math import prod

def solution(num_list):
    # res1, res2 = 0, 1
    # if len(num_list) > 10:
    #     for num in num_list:
    #         res1 += num
    #     return res1
    # else:
    #     for num in num_list:
    #         res2 *= num
    #     return res2
    
    return sum(num_list) if len(num_list) > 10 else prod(num_list)

    