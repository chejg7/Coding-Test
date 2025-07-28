def solution(myString):
    answer = ''.join(["l" if s in "abcdefghijk" else s for s in myString ])
    return answer