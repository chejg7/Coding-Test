def solution(myString):
    
    return ''.join('A' if s.lower() == 'a' else s.lower() for s in myString)