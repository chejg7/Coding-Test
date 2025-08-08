def solution(myString, pat):
    answer = 1 if pat in "".join(["A" if s == "B" else "B" for s in myString]) else 0
    return answer