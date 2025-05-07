def solution(score):
    avg = [(s[0] + s[1]) / 2 for s in score]
    avg_sorted = sorted(avg, reverse=True)
    answer = [avg_sorted.index(a) + 1 for a in avg]
    return answer