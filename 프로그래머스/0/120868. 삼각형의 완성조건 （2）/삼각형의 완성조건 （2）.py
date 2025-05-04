def solution(sides):
    answer = 0
    for i in range(1, sides[0] + sides[1]):
        tri = sorted([i, sides[0], sides[1]])
        if tri[2] < tri[0] + tri[1]:
            answer += 1
    
    return answer