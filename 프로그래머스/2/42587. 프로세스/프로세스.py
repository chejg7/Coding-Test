from collections import deque

# 파이썬에서 deque를 사용하는 이유는, list와 비교해 연산 속도와 성능이 뛰어나기 때문입니다. deque는 스택과 큐의 기능을 모두 갖추고 있어, 양쪽 끝에서 요소를 삽입하거나 삭제할 수 있습니다. 

def solution(priorities, location):
    
    p = [(i, n) for i, n in enumerate(priorities)]
    
    i = 1
    while p:
        if p[0][1] >= max(p, key = lambda x : x[1])[1]:
            if p[0][0] == location:
                break
            del p[0]
            i += 1
        else:
            p.append(p[0])
            del p[0]
        
    return i