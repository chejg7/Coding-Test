def solution(myString):
    # answer = ''.join(["l" if s in "abcdefghijk" else s for s in myString ])
    answer = ''.join([x if x > 'l' else 'l' for x in myString])
    
    return answer