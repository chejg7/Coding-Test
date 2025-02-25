def solution(triangle):
    # answer = triangle[0][0]
    # cur = 0
    # for t in triangle[1:]:
    #     if t[cur] < t[cur + 1]:
    #         cur += 1
    #     answer += t[cur]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            elif triangle[i - 1][j - 1] > triangle[i - 1][j]:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += triangle[i - 1][j]
    answer = max(triangle[-1])
    return answer