def solution(dots):
    a, b, c, d = dots
    answer = abs(max(a[0], b[0], c[0], d[0]) - min(a[0], b[0], c[0], d[0])) * abs(max(a[1], b[1], c[1], d[1]) - min(a[1], b[1], c[1], d[1]))
    return answer