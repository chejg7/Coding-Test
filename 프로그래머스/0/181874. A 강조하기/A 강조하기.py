def solution(myString):
    # return ''.join('A' if s.lower() == 'a' else s.lower() for s in myString)
    return myString.lower().replace('a', 'A')
