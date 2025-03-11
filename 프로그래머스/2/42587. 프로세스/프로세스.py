# def solution(priorities, location):
    
#     p = [(i, n) for i, n in enumerate(priorities)]
    
#     i = 1
#     while p:
#         if p[0][1] >= max(p, key = lambda x : x[1])[1]:
#             if p[0][0] == location:
#                 break
#             del p[0]
#             i += 1
#         else:
#             p.append(p[0])
#             del p[0]
        
#     return i

# 파이썬에서 deque를 사용하는 이유는, list와 비교해 연산 속도와 성능이 뛰어나기 때문입니다. deque는 스택과 큐의 기능을 모두 갖추고 있어, 양쪽 끝에서 요소를 삽입하거나 삭제할 수 있습니다. 
# 위의 코드도 통과하지만 파이썬의 리스트를 사용하기에 효율성 면에서 떨어짐. 

from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))  # (index, priority) 형태로 저장
    order = 0  # 몇 번째로 출력되는지 카운트

    while queue:
        cur = queue.popleft()
        
        if any(cur[1] < p[1] for p in queue):  # 뒤에 더 높은 우선순위가 있는지 확인
            queue.append(cur)  # 맨 뒤로 보냄
        else:
            order += 1  # 출력 순서 증가
            if cur[0] == location:  # 목표 문서라면 반환
                return order
