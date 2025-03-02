def solution(dots):
    inc_dict = {}
    
    # 첫 번째 풀이
#     for i in range(len(dots)):
#         for j in len(dots):
#             if i == j: # 같은 경우만 걸러내기 때문에 대칭성이 있는 두 개의 기울기를 중복 계산하는 문제가 있음
#                 continue

#             dx = dots[i][0] - dots[j][0]
#             dy = dots[i][1] - dots[j][1]
#             inc = dy / dx 
#             if inc in inc_dict:
#                 inc_dict[inc] += 1
#             else:
#                 inc_dict[inc] = 1
#     answer = 1 if len([k for k, v in inc_dict.items() if v == 2]) == 2 else 0
    
    
    # 두 번째 풀이
    
    # for i in range(len(dots)):
    #     for j in range(i + 1, len(dots)):
    #         dx = dots[i][0] - dots[j][0]
    #         dy = dots[i][1] - dots[j][1]
    #         inc = dy / dx # 이 문제에서는 발생하지 않지만 일반적으로는 0으로 나누는 문제가 발생할 수 있음. 이를 방지하기 위해서는 inc = float('inf') if dx == 0 else dy / dx 의 방식으로 작성할 수 있음
    #         if inc in inc_dict:
    #             inc_dict[inc] += 1
    #         else:
    #             inc_dict[inc] = 1
    # answer = 1 if any(v > 1 for v in inc_dict.values()) else 0
    
    
    # 세 번째 풀이
    
#     import math
    
#     slopes = set()
#     for i in range(len(dots)):
#         for j in range(i + 1, len(dots)):
#             dx = dots[i][0] - dots[j][0]
#             dy = dots[i][1] - dots[j][1]
#             gcd = math.gcd(dx, dy)
#             slope = float('inf') if dx == 0 else (dy // gcd, dx // gcd)
#             if slope in slopes:
#                 return 1
#             else:
#                 slopes.add(slope)
    
    
    # 네 번째 풀이
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    if (y1 - y2) / (x1 - x2) == (y3 - y4) / (x3 - x4):
        return 1
    if (y1 - y3) / (x1 - y3) == (y2 - y4) / (x2 - x4):
        return 1
    if (y1 - y4) / (x1 - x4) == (y2 - y3) / (x2 - x3):
        return 1
    
    return 0

# slopes 집합을 사용하여 중복을 방지하면서도 빠르게 같은 기울기를 탐색
# 기울기가 이미 존재하면 바로 1을 반환하여 불필요한 계산 방지
# 모든 점 쌍의 기울기를 저장하여 비교
# (5,3)−(7,4)의 기울기는 (2-1)/(3-1) = 0.5 와 (4-3)/(7-5) = 0.5로 같아야 하지만, 부동소수점 오차가 발생하면 다른 값으로 저장될 가능성이 있음. -> 해결책: 기울기를 dy / dx 대신 **기울기의 "정수 형태 비율"**로 저장해야 함.
# 그러나 여전히 계속해서 실패하는 테스트 케이스가 있음. 어차피 4개의 점이기 때문에 하드코딩으로 비교해도 됨. 